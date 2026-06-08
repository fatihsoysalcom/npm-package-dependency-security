# npm package dependency security

This Python script demonstrates how to use the 'npm audit --json' command to programmatically check for known security vulnerabilities in Node.js package dependencies. It simulates checking a local project's dependencies, highlighting the importance of supply chain security.

## Language

`python`

## How to Run

1. Ensure Node.js and npm are installed and in your PATH.
2. Create a directory, navigate into it, run 'npm init -y', and install a package (e.g., 'npm install lodash@4.17.10').
3. Save the Python code as 'check_dependencies.py' in the same directory.
4. Run the script: 'python check_dependencies.py'.

## Original Article

This example accompanies the Turkish article: [Red Hat npm Olayı: Her Geliştiricinin Bilmesi Gerekenler ve Tedbirler](https://fatihsoysal.com/blog/red-hat-npm-olayi-her-gelistiricinin-bilmesi-gerekenler-ve-tedbirler/).

## License

MIT — see [LICENSE](LICENSE).
