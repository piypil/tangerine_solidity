// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

contract Demo {
    uint[10] public items;
    uint[3][3] public matrixItems;

    function testArray() public {
        items[0] = 100;
        items[1] = 200;
        items[2] = 300;
        items[3] = 400;
        items[4] = 500;
    }

    function testArrayMatrix() public {
        matrixItems = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ];
    }

    uint[] public freeArray;
    uint public len;

    function freeArrayTest() public {
        freeArray.push(4);
        freeArray.push(5);
        len = freeArray.length;
    }

    function sampleMemory() public view returns(uint[] memory){
        uint[] memory tempArray = new uint[](10);
        tempArray[0] = 1;
        return tempArray;
    }
}
