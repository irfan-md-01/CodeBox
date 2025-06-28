# CodeBox 

**Online IDE for Multi-Language Code Execution**

An online compiler built with Django that supports Python, C++, and Java code execution with input handling, persistent code storage, and a user-friendly editor using CodeMirror.

## 🚀 Features

- ✅ **Multi-Language Support**: Python, C++, and Java compilation & execution
- ✅ **Advanced Code Editor**: Syntax highlighting with CodeMirror integration
- ✅ **Custom Input Support**: Handle user input for interactive programs
- ✅ **Persistent Code Storage**: Code is retained between sessions
- ✅ **Error Handling**: Manages infinite loops & Time Limit Exceeded (TLE) errors
- ✅ **Dedicated Language Pages**: Separate execution environments for each language

## 📝 Usage

1. **Select Language**: Choose from Python, C++, or Java
2. **Write Code**: Use the syntax-highlighted editor to write your program
3. **Add Input**: Provide custom input if your program requires it
4. **Execute**: Click "Run Code" to compile and execute your program
5. **View Results**: Output appears below the editor with execution details

## 🔧 Tech Stack

- **Backend**: Django (Python web framework)
- **Frontend**: HTML, CSS, JavaScript with CodeMirror editor
- **Code Execution**: Python subprocess module for secure execution
- **Styling**: Modern responsive design

## 🛠️ How It Works

### Language Execution Details

- **Python Execution**: 
  - Runs using the system's `python3` interpreter
  - Direct execution of `.py` files

- **C++ Execution**: 
  - Compiles source code using `g++` compiler
  - Executes the compiled binary

- **Java Execution**: 
  - Compiles source code using `javac` compiler
  - Runs the compiled class files using `java` runtime

### Security & Performance Features

- **Time Limit Exceeded (TLE) Handling**: Uses subprocess timeout to prevent infinite loops
- **Secure Execution Environment**: Isolated code execution using subprocess
- **Error Handling**: Comprehensive error reporting for compilation and runtime errors

## 🚦 Getting Started

### Prerequisites

- Python 3.x
- Django
- GCC compiler (for C++)
- Java JDK (for Java support)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd codebox
   ```

2. Install dependencies:
   ```bash
   pip install django
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

4. Open your browser and navigate to `http://localhost:8000`

## 📁 Project Structure

```
codebox/
├── manage.py
├── codebox/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── compiler/
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── static/
│   ├── css/
│   ├── js/
│   └── codemirror/
└── README.md
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔮 Future Enhancements

- [ ] Support for additional programming languages
- [ ] User authentication and code saving
- [ ] Collaborative coding features
- [ ] Advanced debugging tools
- [ ] Mobile-responsive improvements
- [ ] Docker containerization for better security

## 🐛 Known Issues

- Large file uploads may cause timeout issues
- Memory-intensive programs may hit system limits

## 📞 Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

---

**Built with ❤️ using Django and CodeMirror**