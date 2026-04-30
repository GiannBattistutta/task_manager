# Task Manager

A terminal-based task manager built with Python.  
This project demonstrates object-oriented programming, JSON file persistence, input validation, task management logic and basic data organization.

## Features

- Add new tasks
- List all tasks
- Mark tasks as completed
- Remove tasks
- Show task statistics
- Save tasks to a JSON file
- Load saved tasks when the program starts

## Technologies Used

- Python
- JSON
- Object-Oriented Programming
- File handling
- Git
- GitHub

## How It Works

The program stores tasks in a local JSON file.  
Each task includes an ID, title, description, completion status, creation date and completion date.

## Task Object Example

```json
{
  "id": 1,
  "title": "Study Python",
  "description": "Practice object-oriented programming",
  "completed": false,
  "created_at": "2026-04-23T10:30:45.123456",
  "completed_at": null
}
