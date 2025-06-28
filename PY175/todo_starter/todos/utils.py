def complete_all_todos(lst):
    for todo in lst['todos']:
        todo['completed'] = True

    return None

def delete_todo_by_id(todo_id, lst):
    lst['todos'] = [todo for todo in lst['todos'] if todo['id'] != todo_id]

def error_for_list_title(title, lists):
    if any(lst['title'] == title for lst in lists):
        return "The title must be unique"
    if not 1 <= len(title) <= 100:
        return "The title must be between 1 and 100 characters"
    return None

def error_for_todo_title(title):
    if not 1 <= len(title) <= 100:
        return "The title must be between 1 and 100 characters"
    return None

def find_list_by_id(list_id, lists):
    return next((lst for lst in lists if lst['id'] == list_id), None)

def find_todo_by_id(todo_id, lst):
    return next((todo for todo in lst if todo['id'] == todo_id), None)

def is_list_completed(lst):
    return len(lst['todos']) > 0 and todos_remaining(lst) == 0

def is_todo_completed(todo):
    return todo['completed']

def sort_lists(lists):
    sorted_lists = sorted(lists, key=lambda lst: lst['title'].casefold())

    incomplete = [lst for lst in sorted_lists if not is_list_completed(lst)]
    complete = [lst for lst in sorted_lists if is_list_completed(lst)]

    return incomplete + complete

def sort_todos(todos):
    sorted_todos = sorted(todos)

    incomplete = [todo for todo in sorted_todos if not is_todo_completed(todo)]
    complete = [todo for todo in sorted_todos if is_todo_completed(todo)]

    return incomplete + complete

def sort_items(items, select_completed):
    sorted_items = sorted(items, key=lambda item: item['title'].lower())

    incomplete_items = [item for item in sorted_items if not select_completed(item)]
    complete_items = [item for item in sorted_items if select_completed(item)]

    return incomplete_items + complete_items

def todos_remaining(lst):
    return sum(1 for todo in lst['todos'] if not todo['completed'])