def read_tasks_from_file(filepath= "data.txt"):
    try:
        with open(filepath, "r") as file:
            tasks = []
            for line in file:
                clean_line = line.strip()
                if clean_line:
                    tasks.append(line)
            return tasks
    except FileNotFoundError:
        return ["Error: Task file not found"]

    except Exception as e:
        return [f"Error loading tasks: {e}"]