import csv
import random
import string
import os
import re

# Configuration
SCHEMA_FILE = 'schema.txt'  # Schema definition file
OUTPUT_DIR = 'output'  # Directory where CSV files will be saved
LOADING_JOB_FILE = 'loading_job.gsql'  # Output file for the loading job
GRAPH_NAME = 'AntiFraud'  # Graph name for which the loading job is created

def parse_schema(schema_file):
    """Parse the schema definition from a text file."""
    schema = {"VertexTypes": [], "EdgeTypes": []}

    with open(schema_file, 'r') as file:
        content = file.read()

    # Regular expressions to match vertex and edge definitions
    vertex_pattern = re.compile(r'Add VERTEX (\w+)\(PRIMARY_ID (\w+) (\w+), (.+?)\) WITH', re.DOTALL)
    edge_pattern = re.compile(r'Add UNDIRECTED EDGE (\w+)\(FROM (\w+), TO (\w+).*\);')

    # Extract vertices
    for match in vertex_pattern.finditer(content):
        vertex_name = match.group(1)
        primary_id_name = match.group(2)
        primary_id_type = match.group(3)
        attributes_str = match.group(4)

        attributes = [{"AttributeName": primary_id_name, "AttributeType": primary_id_type}]
        for attr in attributes_str.split(','):
            attr = attr.strip()
            attr_name, attr_type = attr.split()[:2]
            attributes.append({"AttributeName": attr_name, "AttributeType": attr_type})

        schema["VertexTypes"].append({"Name": vertex_name, "Attributes": attributes})

    # Extract edges
    for match in edge_pattern.finditer(content):
        edge_name = match.group(1)
        from_vertex = match.group(2)
        to_vertex = match.group(3)

        schema["EdgeTypes"].append({"Name": edge_name, "From": from_vertex, "To": to_vertex, "Attributes": []})

    return schema

def generate_random_value(data_type):
    """Generate a random value based on attribute data type."""
    if data_type == 'STRING':
        return generate_random_string()
    elif data_type in ['UINT', 'INT']:
        return random.randint(1, 10000)
    elif data_type == 'FLOAT':
        return round(random.uniform(1.0, 100.0), 2)
    elif data_type == 'DOUBLE':
        return round(random.uniform(1.0, 10000.0), 2)
    elif data_type == 'BOOL':
        return random.choice([True, False])
    elif data_type == 'DATETIME':
        return '2024-09-05T12:00:00'  # Example date-time; can be randomized
    else:
        return None

def generate_random_string(length=8):
    """Generate a random string of fixed length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_data_from_schema(schema):
    """Generate data entries based on the parsed schema and write to CSV."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    for vertex in schema.get('VertexTypes', []):
        vertex_file = os.path.join(OUTPUT_DIR, f"{vertex['Name']}_vertices.csv")
        with open(vertex_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            headers = [attr['AttributeName'] for attr in vertex['Attributes']]
            writer.writerow(headers)
            
            for _ in range(10):  # Generate 10 sample records for testing
                row = [generate_random_value(attr['AttributeType']) for attr in vertex['Attributes']]
                writer.writerow(row)
        print(f"Generated data for vertex '{vertex['Name']}' written to {vertex_file}")
        
    for edge in schema.get('EdgeTypes', []):
        edge_file = os.path.join(OUTPUT_DIR, f"{edge['Name']}_edges.csv")
        with open(edge_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            headers = ['from_id', 'to_id']  # Source and target IDs for edges
            writer.writerow(headers)
            
            for _ in range(10):  # Generate 10 sample records for testing
                row = [generate_random_string(10), generate_random_string(10)]
                writer.writerow(row)
        print(f"Generated data for edge '{edge['Name']}' written to {edge_file}")

def create_loading_job_file(schema):
    """Create a loading job file based on the generated data and schema."""
    with open(LOADING_JOB_FILE, 'w') as file:
        # Step 1: Use graph
        file.write(f'# 1. Use graph\n')
        file.write(f'USE GRAPH {GRAPH_NAME}\n\n')

        # Step 2: Create loading job
        file.write(f'# 2. Create loading job\n')
        file.write('SET sys.data_root="mock_data"\n')
        file.write(f'CREATE LOADING JOB loading_job FOR GRAPH {GRAPH_NAME} {{\n')

        # Define filenames and load statements for each CSV file
        for vertex in schema.get('VertexTypes', []):
            filename_var = f'file_{vertex["Name"].lower()}'
            file_path = f'$sys.data_root/{vertex["Name"]}_vertices.csv'
            
            # Define the file variable
            file.write(f'    DEFINE FILENAME {filename_var}="{file_path}";\n')
            
            # Generate the LOAD statement
            column_list = ', '.join(f'${i}' for i in range(len(vertex['Attributes'])))
            load_statement = f'    LOAD {filename_var} TO VERTEX {vertex["Name"]} VALUES({column_list}) USING SEPARATOR=",", HEADER="true", EOL="\\n";\n'
            
            file.write(load_statement)

        for edge in schema.get('EdgeTypes', []):
            filename_var = f'file_{edge["Name"].lower()}'
            file_path = f'$sys.data_root/{edge["Name"]}_edges.csv'
            
            # Define the file variable
            file.write(f'    DEFINE FILENAME {filename_var}="{file_path}";\n')
            
            # Generate the LOAD statement
            column_list = ', '.join(f'${i}' for i in range(2))  # Assuming 'from_id' and 'to_id'
            load_statement = f'    LOAD {filename_var} TO EDGE {edge["Name"]} VALUES({column_list}) USING SEPARATOR=",", HEADER="true", EOL="\\n";\n'
            
            file.write(load_statement)

        # Close the loading job definition
        file.write('}\n\n')

        # Step 3: Run loading job
        file.write('# 3. Run loading job\n')
        file.write('RUN LOADING JOB loading_job\n\n')

        # Step 4: Drop loading job
        file.write('# 4. Drop loading job\n')
        file.write('DROP JOB loading_job\n')

    print(f"Loading job file '{LOADING_JOB_FILE}' created successfully.")

def main():
    # Parse the schema from the schema file
    schema = parse_schema(SCHEMA_FILE)
    
    # Generate data based on the parsed schema
    generate_data_from_schema(schema)
    
    # Create the loading job file
    create_loading_job_file(schema)

if __name__ == "__main__":
    main()
