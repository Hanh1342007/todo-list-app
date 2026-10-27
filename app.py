tasks = []

def add_task(task_name):
    """Them mot cong viec moi vao danh sach."""
    tasks.append(task_name)
    print(f"Da them cong viec: '{task_name}'")

def show_tasks():
    """Hien thi danh sach cong viec."""
    print("\nDanh sach cong viec:")

    if not tasks:
        print("Chua co cong viec nao.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

if __name__ == "__main__":
    print("Chao mung den voi ung dung To-Do List!")
    add_task("Hoc bai Git va GitHub")
    add_task("Lam bai tap thuc hanh o nha")
    show_tasks()
