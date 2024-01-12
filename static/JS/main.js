let navbar = document.getElementsByTagName('nav')[0];
        let h1 = document.getElementsByClassName('nav-logo');
        let whites = document.querySelectorAll('.white');

        window.onscroll = function () {
            let color, bgColor;
            if (window.scrollY > 0) {
                color = '#f2f2f2';
               bgColor = '#555';
            } else {
                color = '#555';
                bgColor = '#f4f4f4';
            }

            navbar.style.background = bgColor;
            h1.style.color = color;
            whites.forEach(function (white) {
                white.style.color = color;
            });
        }


        function calculateSIP() {
            var amountinvested = document.querySelector(".amount");
            var rateofreturn = document.querySelector(".rate");
            var time = document.querySelector(".years");

            if (!amountinvested.value || isNaN(amountinvested.value) || !rateofreturn.value || isNaN(rateofreturn
                    .value) || !time.value || isNaN(time.value)) {
                alert("Please enter valid numbers in all fields.");
                return;
            }
            var monthlyrate = rateofreturn.value / 12 / 100;
            var months = time.value * 12;
            var futurevalue = 0;
            futurevalue = amountinvested.value * (Math.pow(1 + monthlyrate, months) - 1) / monthlyrate;
            var amounttotalinvested = amountinvested.value * months;
            document.getElementById("amount").innerHTML = "₹" + amounttotalinvested;
            document.getElementById("futurevalue").innerHTML = "₹" + Math.round(futurevalue > 0 ? futurevalue : 0);
        }

        // gst calculator
        function calculateGST() {
            var amount = parseFloat(document.getElementById('gstamount').value) || 0;
            var dropdown = document.querySelector('.gstdropdown');
            var gstPercentage = parseFloat(dropdown.options[dropdown.selectedIndex].value) || 0;
            var total = amount + (amount * gstPercentage / 100);
            document.getElementById('gsttotal').value = total.toFixed(2);
        }


        // income tax calculator
        function calculateTax() {
            var income = document.getElementById("income").value;
            var taxPercentage = document.getElementById("taxPercentage").value;

            var tax = 0;

            if (income <= 250000) {
                tax = 0;
            } else if (income <= 500000) {
                tax = (income - 250000) * (taxPercentage / 100);
            } else if (income <= 1000000) {
                tax = 12500 + (income - 500000) * (taxPercentage / 100);
            } else {
                tax = 112500 + (income - 1000000) * (taxPercentage / 100);
            }

            var resultElement = document.getElementById("result");
            resultElement.innerHTML = "<p>Your income tax is: Rs. " + tax.toFixed(2) + "</p>";
        }



