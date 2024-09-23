from flask import Flask, request, render_template, jsonify
from web3 import Web3, HTTPProvider
import json
import urllib3

app = Flask(__name__)

# Connect to Ganache
blockchain = 'http://127.0.0.1:7545'
web3 = Web3(HTTPProvider(blockchain))

if not web3.isConnected():
    raise Exception("Failed to connect to the Ethereum network.")

# Function to connect to the contract
def connect():
    web3.eth.defaultAccount = web3.eth.accounts[0]  # Set default account
    artifact = "../build/contracts/ProductIdentification.json"  # Adjust path as needed
    with open(artifact) as f:
        artifact_json = json.load(f)
        contract_abi = artifact_json['abi']
        contract_address = artifact_json['networks']['5777']['address']  # Adjust network ID if necessary

    contract = web3.eth.contract(
        abi=contract_abi,
        address=contract_address
    )
    return contract, web3

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/addProduct', methods=['POST'])
def add_product():
    try:
        product_name = request.args.get('product_name')
        manufacturer = request.args.get('manufacturer')
        serial_number = request.args.get('serial_number')

        if not product_name or not manufacturer or not serial_number:
            return "Product name, manufacturer, and serial number are required.", 400

        contract, web3 = connect()
        tx_hash = contract.functions.setProductIdentification(product_name, manufacturer, serial_number).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)
        return 'Product Identification Added Successfully'
    except Exception as e:
        return f'Transaction Error: {str(e)}', 500

@app.route('/verifyProduct', methods=['GET'])
def verify_product():
    product_owner = request.args.get('owner')
    
    contract, web3 = connect()
    try:
        product = contract.functions.getProductIdentification(product_owner).call()
        return jsonify({
            'product_name': product[0],
            'manufacturer': product[1],
            'serial_number': product[2],
            'is_authentic': True  # Assuming it’s authentic if found
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)