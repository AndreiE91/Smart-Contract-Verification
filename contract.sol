// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.7;

contract GetSendContract {
    
    string public farmerName;
    string public lenderName = "Lender A";
    uint internal amount = 200000;
    uint public borrowedAmount;

    function changeAmount(uint _amount) external {
        amount = _amount;
    }

    function borrowFunc(uint _borrowedAmount) external {
        borrowedAmount = _borrowedAmount;
    }
    
}