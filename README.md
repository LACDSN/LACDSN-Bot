<div align="center">
    <img src="docs/resources/tux.gif" width=128 height=128></img>
    <h1>Tux</h1>
    <h3><b>A Discord bot for the All Things Linux Discord server</b></h3>
</div>

<div align="center">
    <p align="center">
        <a href="https://github.com/allthingslinux/tux/forks">
            <img alt="Forks" src="https://img.shields.io/github/commit-activity/m/allthingslinux/tux?style=for-the-badge&logo=git&color=EBA0AC&logoColor=EBA0AC&labelColor=302D41"></a>
        <a href="https://github.com/allthingslinux/tux">
            <img alt="Repo size" src="https://img.shields.io/github/repo-size/allthingslinux/tux?style=for-the-badge&logo=github&color=FAB387&logoColor=FAB387&labelColor=302D41"/></a>
        <a href="https://github.com/allthingslinux/tux/issues">
            <img alt="Issues" src="https://img.shields.io/github/issues/allthingslinux/tux?style=for-the-badge&logo=githubactions&color=F9E2AF&logoColor=F9E2AF&labelColor=302D41"></a>
        <a href="https://opensource.org/license/unlicense/">
            <img alt="License" src="https://img.shields.io/github/license/allthingslinux/tux?style=for-the-badge&logo=gitbook&color=A6E3A1&logoColor=A6E3A1&labelColor=302D41"></a>
        <a href="https://discord.gg/lacommunity">
            <img alt="Discord" src="https://img.shields.io/discord/1172245377395728464?style=for-the-badge&logo=discord&color=B4BEFE&logoColor=B4BEFE&labelColor=302D41"></a>
    </p>
</div>

# NOTE: This bot is OSS, forked From attthingslinux/tux [ATL](https://discord.gg/linux) but has been heavily modified so that it can be used to help in the [LACDSN](https://discord.gg/lacommunity) (Los Angeles Community Discord Server Network) in the same way that it has helped the ALT Server. We are also working with [Wick](https://wick.bot) so that we can have the bots work together in the Servers, rather than against each other.

## About

Tux is a Discord bot for the All Things Linux Discord server. It is designed to provide a variety of features to the server, including moderation, support, utility, and various fun commands. The bot is written in Python using the discord.py library.


## Installation

### Prerequisites
- Python 3.12
- [Poetry](https://python-poetry.org/docs/)

### Steps
1. Clone the repository
   
   ```bash
   gh repo clone lacdsn/lacdsn-bot && cd lacdsn-bot
   ```
2. Install the dependencies
    ```bash
    poetry install
    ```
3. Activate the virtual environment
    ```bash
    poetry shell
    ```
4. Install the pre-commit hooks
    ```bash
    pre-commit install
    ```
5. Generate the prisma client
    ```bash
    prisma generate
    ```
6. Copy the `.env.example` file to `.env` and fill in the required values
    ```bash
    cp .env.example .env
    ```
7. Run the sync command in the server to sync the slash command tree.
   ```
   {prefix}sync <server id>
   ```
8. Review all useful CLI commands by visiting the [useful CLI commands](docs/CLI.md) file.
   

## License
This project is licensed under the terms of the The Unlicense license. See the [LICENSE](LICENSE.md) file for details.
