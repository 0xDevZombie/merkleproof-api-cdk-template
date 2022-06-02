const { MerkleTree } = require('merkletreejs');
const keccak256 = require('keccak256');

const addresses = require('./addresses.json');
const hashedAddresses = addresses.map(addr => keccak256(addr));
const merkleTree = new MerkleTree(hashedAddresses, keccak256, { sortPairs: true });

exports.handler = async (event) => {
    const [_, address] = event.path.split("/");
    const hashedAddress = keccak256(address);
    const proof = merkleTree.getHexProof(hashedAddress);

    return {
        statusCode: 200,
        headers: {
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET"
        },
        body: JSON.stringify(proof)
    };
};