const fortunes = [
  "Take the leap today — your future self will thank you.",
  "A challenge awaits you; face it and grow stronger.",
  "Your hard work will soon pay off — stay persistent.",
  "Trust yourself, even if the path seems uncertain.",
  "Step out of your comfort zone; greatness is on the other side.",
  "An opportunity to shine is coming — be ready.",
  "Your determination today shapes your destiny tomorrow.",
  "Believe in your potential; others will follow your lead.",
  "Mistakes are lessons in disguise — embrace them.",
  "Your passion will ignite something incredible today.",
  "Reflect on your choices; clarity will emerge.",
  "Take responsibility for what you can change.",
  "Growth is uncomfortable, but necessary — lean in.",
  "Let go of what holds you back to move forward.",
  "A bold decision today will redefine your path.",
  "The answers you seek are hidden in action, not thought.",
  "Push past fear; the reward is worth it.",
  "Your mindset today sets the tone for the next month.",
  "Seek discomfort — it's where transformation lives.",
  "A mentor or guide may appear when least expected.",
  "Ignoring your intuition could lead to regret.",
  "A hidden truth may reveal itself suddenly.",
  "Someone may not be what they seem — stay alert.",
  "A sudden change is coming; brace yourself.",
  "Beware of complacency; the world won't wait for you.",
  "Secrets could surface that challenge your beliefs.",
  "An unexpected confrontation may test your resolve.",
  "Avoid distractions; danger lurks in negligence.",
  "Your choices have consequences you cannot ignore.",
  "The path you avoid may hold your destiny."
];

function getRandomFortune() {
  return fortunes[Math.floor(Math.random() * fortunes.length)];
}

function getZodiac(day, month) {
  month = month.toLowerCase();
  if ((month === "march" && day >= 21) || (month === "april" && day <= 19)) return "Aries";
  if ((month === "april" && day >= 20) || (month === "may" && day <= 20)) return "Taurus";
  if ((month === "may" && day >= 21) || (month === "june" && day <= 20)) return "Gemini";
  if ((month === "june" && day >= 21) || (month === "july" && day <= 22)) return "Cancer";
  if ((month === "july" && day >= 23) || (month === "august" && day <= 22)) return "Leo";
  if ((month === "august" && day >= 23) || (month === "september" && day <= 22)) return "Virgo";
  if ((month === "september" && day >= 23) || (month === "october" && day <= 22)) return "Libra";
  if ((month === "october" && day >= 23) || (month === "november" && day <= 21)) return "Scorpio";
  if ((month === "november" && day >= 22) || (month === "december" && day <= 21)) return "Sagittarius";
  if ((month === "december" && day >= 22) || (month === "january" && day <= 19)) return "Capricorn";
  if ((month === "january" && day >= 20) || (month === "february" && day <= 18)) return "Aquarius";
  if ((month === "february" && day >= 19) || (month === "march" && day <= 20)) return "Pisces";
  return null;
}

document.getElementById("getHoroscope").addEventListener("click", () => {
  const day = parseInt(document.getElementById("day").value);
  const month = document.getElementById("month").value;
  const resultDiv = document.getElementById("result");

  
  if (!day || !month) {
    resultDiv.textContent = "Please enter both day and month.";
    resultDiv.style.opacity = 1;
    return;
  }
  if (day < 1 || day > 31) {
    resultDiv.textContent = "Please enter a valid day (1-31).";
    resultDiv.style.opacity = 1;
    return;
  }

  const zodiac = getZodiac(day, month);
  if (!zodiac) {
    resultDiv.textContent = "Invalid date entered. Please try again!";
    resultDiv.style.opacity = 1;
    return;
  }

  resultDiv.innerHTML = `<strong>Your sign is ${zodiac}</strong><br>🔮 Fortune: ${getRandomFortune()}`;
  resultDiv.style.opacity = 1; 
});
