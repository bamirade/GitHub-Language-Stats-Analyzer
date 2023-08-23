# GitHub Language Stats Analyzer

GitHub Language Stats Analyzer is a Python script that fetches language statistics from a user's GitHub repositories and calculates the percentage distribution of each language used.

## Prerequisites

- Python 3.x
- `pip` (Python package manager)

## Installation

1. Clone this repository to your local machine using:
    ```bash
    git clone https://github.com/bamirade/GitHub-Language-Stats-Analyzer.git
    ```

2. Navigate to the repository's directory:
    ```bash
    cd GitHub-Language-Stats-Analyzer
    ```

3. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Rename the `.env.example` file to `.env` and fill in your GitHub username.

2. Run the script for public repositories:
    ```bash
    python github_language_stats.py
    ```

3. Run the script for all repositories including private repositories (requires GitHub access token):
    ```bash
    python github_language_stats_with_private.py
    ```

4. The scripts will fetch language statistics from the main branches of your GitHub repositories and display the percentage distribution of each language used. Please note that the statistics are based on the main branches only.

**Note**: When using the script for public repositories, a GitHub access token is not needed. However, if you wish to include private repositories in the analysis, you will need to provide your GitHub access token in the `.env` file.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the script, feel free to open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
