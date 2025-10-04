let birthMonth = "March";  

let symbol, sign;

if (birthMonth === "January") {
  symbol = "♑"; sign = "Capricorn";
} else if (birthMonth === "February") {
  symbol = "♒"; sign = "Aquarius";
} else if (birthMonth === "March") {
  symbol = "♓"; sign = "Pisces";
} else if (birthMonth === "April") {
  symbol = "♈"; sign = "Aries";
} else if (birthMonth === "May") {
  symbol = "♉"; sign = "Taurus";
} else if (birthMonth === "June") {
  symbol = "♊"; sign = "Gemini";
} else if (birthMonth === "July") {
  symbol = "♋"; sign = "Cancer";
} else if (birthMonth === "August") {
  symbol = "♌"; sign = "Leo";
} else if (birthMonth === "September") {
  symbol = "♍"; sign = "Virgo";
} else if (birthMonth === "October") {
  symbol = "♎"; sign = "Libra";
} else if (birthMonth === "November") {
  symbol = "♏"; sign = "Scorpio";
} else if (birthMonth === "December") {
  symbol = "♐"; sign = "Sagittarius";
} else {
  console.log("Invalid month entered.");
}


if (sign) {
  console.log(`Your sign is ${symbol} ${sign}`);
}
