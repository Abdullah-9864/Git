function handleKeyPress(event) {
  if (event.key === "Enter") {
    addTask();
  }
}


let tasks = [];

function addTask() 
{
  const task = document.getElementById("input").value;
  if (task.trim() === "") 
  return;

  tasks.push(task);
  updateTaskList();    // Update the UI
  document.getElementById("input").value = ""; // Clear input
}


function updateTaskList() {
  const taskList = document.getElementById("taskList");
  taskList.innerHTML = ""; // Clear existing tasks

  tasks.forEach((task, index) => {
    const li = document.createElement("li");
    li.textContent = task;
    taskList.appendChild(li);
  });
}
