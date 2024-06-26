pragma solidity ^0.8.0;

contract Notes {
    string private note;

    function storeNote(string memory _note) public {
        note = _note;
    }

    function getNote() public view returns (string memory) {
        return note;
    }
}
