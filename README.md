<h1 align="center">
  Simple Url shortener
</h1>

<div align="center">

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)


</div>
<hr>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#tech-stack">Tech stack</a> •
  <a href="#how-to-use">How To Use</a>
</p>


## Features
- Forms a short url of 5 characters
- Redirects to the main url


## Tech stack
- [Backend](backend/README.md)
- [Frontend]()
- [Postman for API testing](https://www.postman.com/)


## How To Use
<details>

<summary><strong>Use Docker</strong></summary>

1. Firstly clone repo
   ```bash
   git clone git@github.com:mrKazzila/shortener.git
   ```

2. Prepare local env with make
   ```bash
    make prepare_env DB_HOST=your_db_host DB_PORT=your_db_port DB_NAME=your_db_name DB_USER=your_db_user DB_PASSWORD=your_db_pass
   ```

3. Run docker compose with make
   ```bash
   make docker_run
   ```

4. Stop docker compose with make
   ```bash
   make docker_stop
   ```

</details>


<br>
<br>
<p align="center">
  <a href="https://github.com/mrKazzila">GitHub</a> •
  <a href="https://mrkazzila.github.io/resume/">Resume</a> •
  <a href="https://www.linkedin.com/in/i-kazakov/">LinkedIn</a>
</p>
