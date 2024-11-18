# Cryptofolio
#### Description
Cryptofolio: This is the continuation of my [CS50 2024 Final Project](https://github.com/markoksb/crypto_portfolio).<br>
Cryptocurrency trading across multiple exchanges makes it challenging to track performance in a unified way. With coins often distributed across different exchanges and wallets, keeping track of them all can be confusing and may lead to missed opportunities.
I aimed to create an app to simplify tracking of cryptocurrencies across various platforms by aggregating data and providing real-time insights.<br>
For that reason, one can create multiple independent portfolios and add transactions to them. The app keeps track of profits and losses on a currency, portfolio, and user level.<br>
The app was built using Python, Flask, Jinja, JS, HTML, CSS, and SQLite. Additionally, Bootstrap for responsive design, the login_required decorator to secure access, and SQL wrapper introduced during the CS50 course.
While the initial version focuses on core functionality, future enhancements will include:
* Handling of various APIs and their keys to import data from exchanges.
* Blockchain integration to track non-exchange assets.
* The ability to conduct transactions right from the app.

These features will be part of future development, enhancing Cryptofolio's value beyond CS50.

#### Structure
```
cryptofolio/
├── static/                         # Contains static files like CSS, JS, images
│   ├── css/
│   │   └── main.css                # Main stylesheet
│   ├── img/
│   │   └── cross.png               # icon for portfolio deletion
│   └── favicon.ico                 # favorite icon
├── templates/                      # HTML templates for Jinja rendering
│   ├── base.html                   # Base template - html header, footer and navigation
│   ├── currencies.html             # Currency page - a table of the most important coins
│   ├── error.html                  # Displays error messages #memegen
│   ├── imprint.html                # View to legal info
│   ├── index.html                  # Homepage
│   ├── login.html                  # User login form
│   ├── portfolio_del.html          # Portfolio deletion form
│   ├── portfolio_new.html          # Portfolio creation form
│   ├── portfolio_transaction.html  # Form to add or remove a coin
│   ├── portfolio.html              # Portfolio page - Overview and portfolio subnav
│   └── register.html               # User registration form
│   └── transactions.html           # View to transactions
├── app.py                          # Main Flask application - config and routing
├── cgecko.py                       # CoinGecko API implementations
├── currencies.py                   # generates the coin list and updates its prices
├── database_schema.py              # strings to (re-)create the database
├── database.py                     # database functions
├── error.py                        # generates error messages and char escapes
├── key.py                          # contains coingecko api key (not shared)
├── portfolio.db                    # SQLite database file (example data)
├── portfolio.py                    # aggregate and calculate data for each portfolio
├── README.md                       # Documentation file (this file)
├── req_login.py                    # login_required decorator
├── requirements.txt                # Project dependencies
└── users.py                        # handling of user login/logout and registration
```

#### Installation
Follow these steps to install the app on your device. Keep in mind that you will need an API key from [CoinGecko](https://coingecko.com). Currently you can test the app as is on my [server](https://cf.starlight.berlin).
```
git clone https://github.com/markoksb/cryptofolio.git           # clone the repository
cd cryptofolio                                                  # change to the new directory
python3 -m venv venv                                            # create a virtual environment
source venv/bin/activate                                        # activate the environment
pip install -r requirements.txt                                 # install the project dependencies
echo "coingecko_api_key = '<your-coingecko-api-key>' > key.py   # add your own api key (as it's not provided)
python3 app.py                                                  # run the app default run is 127.0.0.1:8080
```

#### Contribute
Feel free to submit pull requests or report issues. :)

#### License
This project is licensed under the MIT License. This means you are free to use, copy, modify, and distribute the software, with the condition that the original license and copyright notice are included. The software is provided "as is," without any warranties, express or implied, including but not limited to merchantability or fitness for a particular purpose.

#### Credits
- **CoinGecko**: API for cryptocurrency data.
- **Flask**: Framework used for building the web app.
- **Bootstrap**: Frontend framework for responsive design.
- **CS50**: For providing the knowledge and skills needed to complete this project. This was CS50. 🦆
