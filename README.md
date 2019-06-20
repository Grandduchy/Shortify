# Shortify

Easily Shorten urls

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites
This project must used python3, python2 is not supported by django framework
```
sudo apt install python3
```

Install package manager pip to install other packages
```
sudo apt install python-pip
```
Finally, install django framework
```
pip install django
```
### Installing

Clone this project

```
git clone https://github.com/Grandduchy/Shortify
cd Shortify
```

Create the migrations necessary for the database

```
python3 manage.py migrate
```

Run the server
```
python3 manage.py runserver
```
The server now runs on http://127.0.0.1:8000/

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [JQuery](https://jquery.com/) - Javascript Library

## Authors

* **Joshua Challenger** - *Complete Project* - [Grandduchy](https://github.com/Grandduchy)
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
