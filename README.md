# Computer-Graphics-Basics
This repo represents my learning of SWE 424(Computer Graphics and Image Processing Lab) course.


## Setup
To open and run a **Python project** that you've cloned from a GitHub repository in **PyCharm**, follow these steps:

### 1. **Clone the GitHub Repository**
If you haven't already cloned the repository, you can do it either from PyCharm or through the terminal.

- **In PyCharm**:
  - Go to `File` → `New Project` → `Get from VCS`.
  - Select **Git** from the dropdown and paste the repository URL.
  - Choose a directory to clone the repository and click **Clone**.

- **Using Terminal**:
  ```bash
  git clone <repository-url>
  cd <project-directory>
  ```

### 2. **Configure the Python Interpreter**
   If your project uses a virtual environment (like the one described in `pyvenv.cfg`), you need to configure it in PyCharm.

   - **Detect existing virtual environment [Initially you won't have any, follow the next step]**:
     - Go to `File` → `Settings` (or `PyCharm` → `Preferences` on macOS).
     - Select `Project: <your-project-name>` → `Python Interpreter` from the sidebar.
     - Click the gear icon next to the interpreter dropdown and choose `Add...`.
     - Select `Existing environment` and navigate to your project’s virtual environment. If your virtual environment is inside the project folder, look for it under the `venv` or `env` folder, and select the `bin/python` (or `Scripts/python.exe` on Windows) file.
     
   - **Create and Activate a Virtual Environment from terminal**
     - Create a Virtual Environment
       1. **Open a terminal** in the root directory of your project (`.../Computer-Graphics-Basics`).
       2. Run the following command to create a virtual environment:
          ```bash
          python -m venv venv
          ```
          This will create a `venv` folder in your project that contains an isolated Python environment.
 
     - Activate a Virtual Environment
       - On Windows:
         ```bash
         .\venv\Scripts\activate
         ```
       - On macOS/Linux:
         ```bash
         source venv/bin/activate
         ```

         After activation, your terminal prompt should change to indicate you're now working within the virtual environment.

### 3. **Install Project Dependencies**
   The project has a `requirements.txt`, you'll need to install the dependencies.

   - **With `requirements.txt`**:
     - PyCharm should automatically detect it and offer to install the dependencies. If not, open the terminal within PyCharm and run:
       ```bash
       pip install -r requirements.txt
       ```

### 4. **Set Up Run Configuration**
   If your project has a main Python script (like `app.py` or `main.py`), you need to set up a **Run Configuration** to easily run the project.

   - Go to `Run` → `Edit Configurations...`.
   - Click the `+` icon to add a new configuration.
   - Choose **Python** as the configuration type.
   - In the **Script path**, select the main script of your project.
   - Set the **Python Interpreter** to the interpreter you configured in step 3.
   - Optionally, you can add any **parameters** or **environment variables** required by your project.
   
   Once configured, you can run the project by selecting the run configuration from the toolbar and clicking the green **Run** button.

### 5. **Run the Project**
   Now, your project should be ready to run. You can:
   - Click the **Run** button (the green triangle in the top-right corner).
   - Or use `Shift + F10` to run the project.

[Sample Generated Figure](opengl-tut/Exam/sampleFigure.md)
--------------------

--------------------# CGI-Lab-Modified
