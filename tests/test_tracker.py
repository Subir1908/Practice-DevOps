from src.tracker import add_task


def test_add_task():
    # 1. Setup
    empty_tasks = []

    # 2. Execute
    updated_tasks = add_task(empty_tasks, "Learn PyTest")

    # 3. Assert (Check if it worked)
    assert len(updated_tasks) == 1
    assert updated_tasks[0]["title"] == "Learn PyTest"
    assert updated_tasks[0]["status"] == "Pending"