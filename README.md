# Resume Optimization Project

## Project Overview

This project automates the process of optimizing a resume to align better with a given job description. Leveraging the capabilities of the OpenAI API, it helps individuals quickly adapt their resumes for different job applications by focusing on key skills and experiences relevant to a specific position.

## Features

- **Automated Resume Optimization**: Adjusts a Markdown-formatted resume based on a provided job description.
- **Keyword Emphasis**: Highlights relevant skills and experiences in the resume based on keywords from the job description.
- **Uses GPT-4o-mini**: Utilizes the OpenAI GPT-4o-mini model to perform the resume enhancement.
- **Output Storage**: Saves the optimized resume in a Markdown file in the `output` directory.

## Project Structure

- **data/**: Contains input data, such as sample resumes and job descriptions.
- **output/**: Stores the output of optimized resumes.
- **scripts/**: Contains the main Python script (`optimize_resume.py`) for optimizing the resume.
- **.env**: Stores sensitive information like the OpenAI API key.
- **README.md**: Provides a project overview and usage instructions.
- **requirements.txt**: Lists all required Python packages.

## Prerequisites

- **Python 3.7+**
- **OpenAI API Key**: Required to interact with the OpenAI API.
- **.env file**: Create a `.env` file in the root directory to store the API key as follows:
  ```
  OPENAI_API_KEY=your_api_key_here
  ```

## Setup Instructions

1. **Clone the Repository**
   ```
   git clone https://github.com/kevinjaegle/resume-optimization.git
   cd resume-optimization
   ```

2. **Create a Virtual Environment**
   ```
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Add the OpenAI API Key**
   - Create a `.env` file in the root directory and add your API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

Run the main script to optimize the resume:
```bash
python scripts/optimize_resume.py
```

The optimized resume will be saved in the `output` directory as `optimized_resume.md`.

## Example

This project provides a sample resume and job description for testing. The main script (`optimize_resume.py`) takes the input data, sends it to OpenAI's GPT-4o-mini model, and outputs a modified resume that better aligns with the job description.

## Contribution

Feel free to submit issues or pull requests. Any contributions to improve the project are welcome!

## License

This project is licensed under the MIT License.

---

**Disclaimer**: This project uses a generative AI model, and while it provides suggestions for enhancing a resume, it's recommended that users review the output carefully to ensure accuracy and appropriateness for their needs.


