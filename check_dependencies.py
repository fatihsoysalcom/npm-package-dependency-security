import subprocess
import json
import sys

def check_npm_dependencies(package_name):
    """Checks for known vulnerabilities in npm package dependencies using npm audit."""
    try:
        # Execute 'npm audit --json' to get vulnerability data in JSON format
        # This command requires Node.js and npm to be installed and in the PATH.
        # It will analyze the dependencies of the specified package.
        result = subprocess.run(
            ["npm", "audit", "--json", f"--prefix={package_name}"],
            capture_output=True,
            text=True,
            check=True
        )
        audit_data = json.loads(result.stdout)

        if audit_data.get("vulnerabilities"):
            print(f"\n--- Vulnerabilities found in {package_name} dependencies ---")
            for severity, vulns in audit_data["vulnerabilities"].items():
                if vulns:
                    print(f"\n{severity.capitalize()}: {len(vulns)} found")
                    for vuln_name, vuln_details in vulns.items():
                        print(f"  - {vuln_name}")
                        # In a real-world scenario, you'd want to inspect vuln_details
                        # for more information like severity, path, and fix versions.
            print("\n--- End of Vulnerabilities ---")
            print("\nConsider updating vulnerable packages or using alternative, secure packages.")
        else:
            print(f"\nNo known vulnerabilities found in {package_name} dependencies.")

    except FileNotFoundError:
        print("Error: Node.js and npm are not found. Please ensure they are installed and in your PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error running npm audit for {package_name}:")
        print(e.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Could not parse npm audit output as JSON.")
        sys.exit(1)

if __name__ == "__main__":
    # This script demonstrates how to programmatically check for npm package vulnerabilities.
    # In a real-world scenario, you would run this against your project's node_modules directory.
    # For this example, we'll simulate by assuming a package is installed locally.
    # To run this, you need to have Node.js and npm installed.
    # 1. Create a dummy npm project: mkdir dummy-npm-project && cd dummy-npm-project
    # 2. Initialize npm: npm init -y
    # 3. Install a package with known vulnerabilities (e.g., an older version of lodash or express)
    #    e.g., npm install lodash@4.17.10
    # 4. Save this Python script in the same directory (e.g., check_dependencies.py)
    # 5. Run this script: python check_dependencies.py

    # The --prefix argument tells npm audit where to look for node_modules.
    # We are using '.' to indicate the current directory (where node_modules would be).
    print("Checking npm dependencies for vulnerabilities...")
    check_npm_dependencies(".")
