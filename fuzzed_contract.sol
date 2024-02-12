Fuzzed contract:// SPDX-License-Identifi L-3.0

prama olidity ^0.8.7;

cntract GetSendContract {
    
    string publicfarmerName;
    string public lenderName = "Lender A";
    uint internal mount = 20000;
    uint public borrowedAmount;

    funcion changAmunt(uint _amount) external {
      mount = _amount;
    }

   function borrowFunc(uint _borrwedAmount) external {
        borrowedmount = _borrowedAmount;
   }
    
