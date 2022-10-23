from web3 import Web3
from solcx import compile_source

compiled_solidity = compile_source(
    '''
    // SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 * @custom:dev-run-script ./scripts/deploy_with_ethers.ts
 */
contract Storage {

    uint256 number;

    /**
     * @dev Store value in variable
     * @param num value to store
     */
    function store(uint256 num) public {
        number = num;
    }

    /**
     * @dev Return value 
     * @return value of 'number'
     */
    function retrieve() public view returns (uint256){
        return number;
    }
}
    ''',
    output_values=['abi', 'bin']
)

contract_id, contract_intreface = compiled_solidity.popitem()

bytecode = contract_intreface['bin']
abi = contract_intreface['abi']

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
address = "0x2b02810592bDAfE4648F78d2900Dd99338E328A7"
print(w3.isConnected())

if w3.eth.accounts[0] == address:
    print(w3.eth.accounts[0])
    w3.eth.default_account == w3.eth.accounts[0]


Storage = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = w3.eth.get_transaction_count(address)
print(nonce)

transaction_information = {
    "chainId": chain_id, 
    "from": address, 
    "nonce": nonce
}

th_hash = Storage.constructor().transact(transaction_information)

tx_receipt = w3.eth.wait_for_transaction_receipt(th_hash)

greeter = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

def storage(uint256):
    nonce = w3.eth.get_transaction_count(address)
    transaction_information = {
        "chainId": chain_id, 
        "from": address, 
        "nonce": nonce
        }
    tx_hash = greeter.functions.store(uint256).transact(transaction_information)

storage(17282)
print(greeter.functions.retrieve().call())
