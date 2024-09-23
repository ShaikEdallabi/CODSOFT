const ProductIdentification = artifacts.require("ProductIdentification");

module.exports = function(deployer) {
  deployer.deploy(ProductIdentification);
};