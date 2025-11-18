import json
import os


def append_dict_to_json(filename, new_dict):
    """
    将一个字典追加到一个 JSON 列表文件中。
    如果文件不存在或为空，则创建包含新字典的列表。
    """
    data = []

    # 1. 尝试读取现有数据
    # 确保文件存在且不为空
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                # 加载现有内容。如果文件是有效的JSON列表，则将其加载到data中。
                data = json.load(f)

                # 检查加载的数据是否是列表，如果不是，我们可能需要将其转换为列表
                if not isinstance(data, list):
                    print(
                        f"Warning: File '{filename}' content is not a list. Resetting to a new list."
                    )
                    data = []

        except json.JSONDecodeError:
            print(
                f"Error: File '{filename}' is corrupted or invalid JSON. Overwriting with new data list."
            )
            data = []
        except Exception as e:
            print(f"An unexpected error occurred during reading: {e}")
            return

    # 2. 追加新字典
    data.append(new_dict)

    # 3. 写回整个更新后的列表
    try:
        with open(filename, "w", encoding="utf-8") as f:
            # 使用 indent 参数美化输出，使其更易读
            json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Successfully appended data to '{filename}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")


def overwrite_json_with_list(filename, list_of_dicts):
    """
    清空（覆盖）指定文件，并将传入的字典列表写入为新的 JSON 内容。

    Args:
        filename (str): 要写入的文件路径。
        list_of_dicts (list): 要写入文件中的字典列表。
    """
    try:
        # 使用 'w' 模式打开文件。这会清空文件或创建新文件。
        with open(filename, "w", encoding="utf-8") as f:
            # 将完整的列表写入文件。
            # ensure_ascii=False 支持中文等非ASCII字符。
            # indent=4 格式化输出，使其易读。
            json.dump(list_of_dicts, f, ensure_ascii=False, indent=4)

        print(f"✅ 文件 '{filename}' 已清空并成功写入 {len(list_of_dicts)} 条新数据。")

    except Exception as e:
        print(f"❌ 写入文件时发生错误: {e}")


if __name__ == "__main__":
    file_path = "config.json"
    new_product = {
        "id": 25,
        "name": "V2rayn",
        "url": "https://github.com/2dust/v2rayN/releases",
        "logo": "https://toolb.cn/favicon/github.com",
        "desc": None,
        "catelog": "常用工具",
        "status": None,
        "sort_order": 9999,
        "create_time": None,
        "update_time": None,
    }

    # 第一次运行会创建文件（或追加到现有文件）
    # append_dict_to_json(file_path, new_product)

    overwrite_json_with_list(file_path, [new_product])
