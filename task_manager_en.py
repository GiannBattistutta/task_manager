import json
import os
from datetime import datetime
from typing import List, Dict

class TaskManager:
    """Task manager with JSON persistence"""
    
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks: List[Dict] = []
        self.load_tasks()
    
    def load_tasks(self) -> None:
        """Load tasks from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.tasks = json.load(f)
            except json.JSONDecodeError:
                self.tasks = []
        else:
            self.tasks = []
    
    def save_tasks(self) -> None:
        """Save tasks to JSON file"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, indent=2, ensure_ascii=False)
    
    def add_task(self, title: str, description: str = "") -> None:
        """Add a new task"""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "completed": False,
            "created_at": datetime.now().isoformat(),
            "completed_at": None
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ Task '{title}' added successfully!")
    
    def list_tasks(self, show_completed: bool = True) -> None:
        """List all tasks"""
        if not self.tasks:
            print("No tasks found.")
            return
        
        tasks_to_show = self.tasks
        if not show_completed:
            tasks_to_show = [t for t in self.tasks if not t["completed"]]
        
        if not tasks_to_show:
            print("No pending tasks.")
            return
        
        print("\n" + "="*60)
        print(f"{'ID':<4} {'Status':<10} {'Task':<30} {'Description':<15}")
        print("="*60)
        
        for task in tasks_to_show:
            status = "✓ Done" if task["completed"] else "⏳ Pending"
            description = task["description"][:15] if task["description"] else "-"
            print(f"{task['id']:<4} {status:<10} {task['title']:<30} {description:<15}")
        
        print("="*60 + "\n")
    
    def mark_completed(self, task_id: int) -> None:
        """Mark a task as completed"""
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print(f"Task {task_id} was already completed.")
                else:
                    task["completed"] = True
                    task["completed_at"] = datetime.now().isoformat()
                    self.save_tasks()
                    print(f"✓ Task '{task['title']}' marked as completed!")
                return
        
        print(f"Task with ID {task_id} not found.")
    
    def remove_task(self, task_id: int) -> None:
        """Remove a task"""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed_task = self.tasks.pop(i)
                # Reorganize IDs
                for j, t in enumerate(self.tasks, 1):
                    t["id"] = j
                self.save_tasks()
                print(f"✓ Task '{removed_task['title']}' removed!")
                return
        
        print(f"Task with ID {task_id} not found.")
    
    def get_statistics(self) -> None:
        """Show task statistics"""
        if not self.tasks:
            print("No tasks to show statistics.")
            return
        
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["completed"])
        pending = total - completed
        
        print("\n" + "="*40)
        print("📊 STATISTICS")
        print("="*40)
        print(f"Total tasks: {total}")
        print(f"Completed tasks: {completed}")
        print(f"Pending tasks: {pending}")
        if total > 0:
            percentage = (completed / total) * 100
            print(f"Progress: {percentage:.1f}%")
        print("="*40 + "\n")
