# Day 1 — Notes

## Making a key pair in AWS

AWS account → EC2 dashboard → **Key pairs** → **Create key pair** → choose name, type,
and export (private key file) format.

It's used for logging in, and for checking that the key you made works:

```bash
aws ec2 describe-key-pairs --key-names <NAME>
```

## Making a user that belongs to a server

1. Log in as a user on the server you want to create the new user on:

   ```bash
   ssh username@your-server-ip
   ```

2. Create the user:

   ```bash
   sudo useradd -s /sbin/nologin <username>
   ```

3. Verify the user was made:

   ```bash
   grep <username> /etc/passwd
   ```

## Questions for feeding my curiosity

1. What is a Python virtual environment?
2. What does the `requirements.txt` file do?
3. Why do you have to activate a Python environment?
4. What does the `pip freeze` command do?

## Steps for setting up the virtual environment for an ML project

1. Make the requirements file:

   ```bash
   touch requirements.txt
   ```

2. Fill the file with the packages needed.

3. Make the virtual environment:

   ```bash
   python3 -m venv venv_name
   ```

4. Activate the environment you made:

   ```bash
   source venv_name/bin/activate
   ```

5. Install the packages:

   ```bash
   pip install -r requirements.txt
   ```

6. Update the requirements file with the package versions:

   ```bash
   pip freeze > requirements.txt
   ```
