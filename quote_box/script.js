const quotes = [
  "Code is like humor. When you have to explain it, it's bad.",
  "First, solve the problem. Then, write the code.",
  "Experience is the name everyone gives to their mistakes.",
  "Hard work beats talent when talent doesn't work hard.",
  "Don't watch the clock; do what it does. Keep going.",
  "Push yourself, because no one else is going to do it for you.",
  "Strive for progress, not perfection.",
  "Success is the sum of small efforts, repeated day in and day out.",
  "Dream it. Wish it. Do it.",
  "The only way to achieve the impossible is to believe it is possible.",
  "Great things are done by a series of small things brought together.",
  "Fall seven times and stand up eight.",
  "Your limitation—it's only your imagination.",
  "Work hard in silence, let success make the noise.",
  "Don't stop when you're tired. Stop when you're done.",
  "It always seems impossible until it's done.",
  "The harder you work for something, the greater you'll feel when you achieve it.",
  "Little by little, one travels far.",
  "Success doesn't come from what you do occasionally, it comes from what you do consistently.",
  "Motivation is what gets you started. Habit is what keeps you going."
];

const quoteText = document.getElementById("quote-text");
const newQuoteBtn = document.getElementById("new-quote-btn");

newQuoteBtn.addEventListener("click", () => {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    quoteText.textContent = quotes[randomIndex];
});
