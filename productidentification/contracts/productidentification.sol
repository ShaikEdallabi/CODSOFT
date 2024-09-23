// Example Solidity contract
pragma solidity ^0.8.0;

contract ProductIdentification {
    struct Product {
        string name;
        string manufacturer;
        bool isAuthentic; // Assuming we are storing authenticity as a boolean
    }

    mapping(string => Product) public products;

    function setProductIdentification(string memory _serialNumber, string memory _name, string memory _manufacturer, bool _isAuthentic) public {
        products[_serialNumber] = Product(_name, _manufacturer, _isAuthentic);
    }

    function getProductIdentification(string memory _serialNumber) public view returns (string memory, string memory, bool) {
        Product memory product = products[_serialNumber];
        return (product.name, product.manufacturer, product.isAuthentic);
    }
}
