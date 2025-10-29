# SAP Business Objects RESTful API Python SDK

A Python SDK for interacting with SAP Business Objects (BO) platform using REST API. This project provides a comprehensive set of tools for managing Business Objects connections, universes, and WebI documents.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Project Structure](#project-structure)
- [Usage Examples](#usage-examples)
- [Authentication](#authentication)
- [API Reference](#api-reference)
- [Logging](#logging)
- [Contributing](#contributing)
- [Version History](#version-history)
- [License](#license)

## 🔍 Overview

This SDK provides a Python interface to interact with SAP Business Objects platform through its REST API. It enables developers to:

- Authenticate with BO platform using username/password or trusted authentication
- Manage universes (UNX and UNV types)
- Perform operations on WebI documents
- Handle data providers and document management
- Comprehensive logging and error handling

## ✨ Features

- **Authentication Management**: Support for both standard and trusted authentication methods
- **Universe Operations**: Retrieve and manage universes, get related reports and connections
- **WebI Document Management**: Create, update, save, and manage WebI documents
- **Data Provider Operations**: Manage data providers within WebI documents
- **Folder Navigation**: Recursive folder traversal and document discovery
- **Session Management**: Persistent session handling for efficient API calls
- **Comprehensive Logging**: Built-in logging capabilities with customizable log levels
- **Error Handling**: Robust error handling with detailed exception information

## 📦 Installation

### Prerequisites

- Python 3.6 or higher
- `requests` library
- Access to SAP Business Objects platform

### Dependencies

```bash
pip install requests
```

### Clone the Repository

```bash
git clone https://github.com/alexraio/SAP_BO_RESTFUL_API.git
cd SAP_BO_RESTFUL_API
```

## 🚀 Quick Start

```python
from sdk_parser_new import BOESDKParser
from rest_helper import setup_logging

# Set up logging
setup_logging(log_dir="logs", log_name="bo_api_demo")

# Initialize the parser
parser = BOESDKParser(
    protocol='http',
    host='your-bo-server.com',
    port='8080'
)

# Authenticate
parser.set_logon_token('username', 'password')

# Get universes
universes = parser.get_universes()
print("Available universes:", universes)

# Logout when done
parser.bo_logoff()
```

## 📚 Documentation

### Configuration

The SDK can be configured during initialization:

```python
parser = BOESDKParser(
    protocol='https',           # http or https
    host='bo-server.domain.com', # BO server hostname
    port='8080',                # Port number
    content_type='application/json'  # Content type for requests
)
```

### Environment Variables

You can set up environment variables for common configurations:

```bash
export BO_HOST=your-bo-server.com
export BO_PORT=8080
export BO_PROTOCOL=https
```

## 📁 Project Structure

```
SAP_BO_RESTFUL_API/
├── sdk_parser_new.py      # Main SDK class (BOESDKParser)
├── rest_helper.py         # Logging utilities
├── logger_function.py     # Custom logging functions
├── sdk_parser.py_bak      # Backup of previous version
├── README.md              # This file
├── .gitignore            # Git ignore configuration
└── __pycache__/          # Python cache files
```

## 💡 Usage Examples

### Authentication Examples

#### Standard Authentication
```python
# Username and password authentication
parser.set_logon_token('your_username', 'your_password')
```

#### Trusted Authentication
```python
# Trusted authentication (for integrated environments)
parser.set_trusted_token('Administrator')
```

### Universe Operations

```python
# Get all universes
universes = parser.get_universes()

# Get universe details
universe_details = parser.get_univ_details('universe_id')

# Get reports related to a universe
univ_id, univ_name, reports = parser.get_universe_related_reports('universe_id')

# Get universe connection ID
connection_id = parser.get_univ_related_conn_id('universe_id')
```

### WebI Document Management

```python
# Get folders recursively
folders = parser.get_folders('root_folder_id')

# Get WebI documents in a folder
webi_docs = parser.get_webi_docs('folder_id')

# Get document details
doc_details = parser.get_doc_details('webi_doc_id')

# Get document status
doc_status = parser.get_doc_status('webi_doc_id')

# Save a WebI document
parser.save_webi_doc('webi_doc_id', 'document_name')
```

### Data Provider Operations

```python
# Get data providers for a document
data_providers = parser.get_dp('webi_doc_id')

# Get specific data provider details
dp_details = parser.get_dp_details('webi_doc_id', 'dp_id')

# Purge a data provider
success = parser.purge_dp('webi_doc_id', 'dp_id')
```

## 🔐 Authentication

The SDK supports two authentication methods:

1. **Standard Authentication**: Using username and password
2. **Trusted Authentication**: Using trusted user credentials (typically for integrated environments)

### Security Notes

- Always use HTTPS in production environments
- Store credentials securely (environment variables, secure vaults)
- Implement proper session management
- Regular token refresh for long-running applications

## 📖 API Reference

### BOESDKParser Class

#### Initialization
```python
BOESDKParser(protocol='http', host='ora-rhel-01.pf.box', port='8080', content_type='application/json')
```

#### Authentication Methods
- `set_logon_token(username, password)`: Standard authentication
- `set_trusted_token(username='Administrator')`: Trusted authentication
- `bo_logoff()`: Logout and close session

#### Universe Methods
- `get_universes()`: Get all available universes
- `get_univ_details(universe_id)`: Get universe details
- `get_universe_related_reports(universe_id)`: Get reports related to universe
- `get_univ_related_conn_id(universe_id)`: Get universe connection ID

#### Document Methods
- `get_folders(folder_id, folder_list=None)`: Get folders recursively
- `get_webi_docs(folder_id, webi_list=None)`: Get WebI documents in folder
- `get_doc_details(webi_doc_id)`: Get document details
- `get_doc_status(webi_doc_id)`: Get document status
- `save_webi_doc(webi_doc_id, webi_doc_name)`: Save WebI document

#### Data Provider Methods
- `get_dp(webi_doc_id)`: Get data providers for document
- `get_dp_details(webi_doc_id, dp_id)`: Get data provider details
- `purge_dp(webi_doc_id, dp_id)`: Purge data provider

## 📝 Logging

The project includes comprehensive logging capabilities:

### Using rest_helper.py
```python
from rest_helper import setup_logging

# Setup logging with custom directory and name
setup_logging(log_dir="custom_logs", log_name="my_application")
```

### Using logger_function.py
```python
from logger_function import log_and_write_output
import logging

# Log messages with different levels
log_and_write_output('output.log', 'Info message', logging.INFO)
log_and_write_output('output.log', 'Warning message', logging.WARNING)
log_and_write_output('output.log', 'Error message', logging.ERROR)
```

### Log Files

- Logs are automatically timestamped
- Default log directory: `logs/`
- Log format: `YYYY-MM-DD HH:MM:SS - LEVEL - MESSAGE`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comprehensive docstrings for all methods
- Include error handling and logging
- Write unit tests for new features
- Update documentation as needed

### Code Style

```python
# Example of expected code style
def method_name(self, parameter_one, parameter_two=None):
    """
    Brief description of the method.
    
    Args:
        parameter_one (str): Description of parameter one.
        parameter_two (str, optional): Description of parameter two.
    
    Returns:
        dict: Description of return value.
    
    Raises:
        Exception: Description of when this exception is raised.
    """
    # Implementation here
    pass
```

## 📈 Version History

### Version 0.1
- **Author**: Ballarin, Alessio
- **Description**: Initial version
- **Features**:
  - Basic BO platform connection
  - Universe management
  - WebI document operations
  - Data provider management
  - Authentication support

### Planned Features

- Enhanced error handling
- Async/await support
- Batch operations
- Performance optimizations
- Extended API coverage

## ⚠️ Known Issues

- SSL certificate verification is disabled (`verify=False`) - should be addressed in production
- Some methods return `None` on error - consider implementing more specific error codes
- Limited error message standardization

## 🔧 Troubleshooting

### Common Issues

1. **Authentication Failures**
   - Verify credentials and server connectivity
   - Check if the BO server is accessible
   - Ensure proper network configuration

2. **Connection Timeouts**
   - Increase timeout values in requests
   - Check network latency
   - Verify server performance

3. **SSL Certificate Issues**
   - Configure proper SSL certificates
   - Update certificate validation settings

### Debug Mode

Enable detailed logging for troubleshooting:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏢 Enterprise Usage

This SDK is designed for enterprise environments using SAP Business Objects. It includes:

- Enterprise-grade error handling
- Session management for long-running processes
- Comprehensive logging for audit trails
- Support for both standard and trusted authentication

## 📞 Support

For support and questions:

- Create an issue in the GitHub repository
- Check the [documentation](#documentation) section
- Review the [API reference](#api-reference)

## 🙏 Acknowledgments

- SAP Business Objects development team for the REST API
- Contributors to the requests library
- Open source community for continuous improvement

---

**Note**: This SDK is designed for SAP Business Objects and requires appropriate licenses and access to the BO platform. Always follow your organization's security guidelines when implementing authentication and handling sensitive data.