const inputBox = document.getElementById("input-box");
const listContainer = document.getElementById("list-container");
const completedCounter = document.getElementById("completed-counter");
const uncompletedCounter = document.getElementById("uncompleted-counter");

function addTask() {
  const task = inputBox.value.trim();
  if (!task) return;

  const li = document.createElement("li");
  li.innerHTML = `
    <span class="task-text">${task}</span>
    <span class="task-buttons">
      <button class="tick-btn">✔️</button>
      <button class="edit-btn">✏️</button>
      <button class="delete-btn">🗑️</button>
    </span>
  `;
  listContainer.appendChild(li);
  inputBox.value = "";

  const taskText = li.querySelector(".task-text");
  const tickBtn = li.querySelector(".tick-btn");
  const editBtn = li.querySelector(".edit-btn");
  const deleteBtn = li.querySelector(".delete-btn");

  // Tick button to mark complete/incomplete
  tickBtn.addEventListener("click", () => {
    li.classList.toggle("completed");
    updateCounters();
  });

  // Edit task
  editBtn.addEventListener("click", () => {
    const update = prompt("Edit task:", taskText.textContent);
    if (update !== null) {
      taskText.textContent = update;
      li.classList.remove("completed");
      updateCounters();
    }
  });

  // Delete task
  deleteBtn.addEventListener("click", () => {
    li.remove();
    updateCounters();
  });

  updateCounters();
}

function updateCounters() {
  const completedTasks = document.querySelectorAll("li.completed").length;
  const uncompletedTasks = document.querySelectorAll("li:not(.completed)").length;

  completedCounter.textContent = completedTasks;
  uncompletedCounter.textContent = uncompletedTasks;
}
