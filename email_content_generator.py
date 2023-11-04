def create_grades_entry(df, student_id):
    # 根据学生ID筛选出该生的所有成绩
    student_grades = df[df['学号'] == student_id]
    # 创建成绩条目的列表
    grades_entry = []
    for _, row in student_grades.iterrows():
        # 检查成绩是否为数值类型
        if isinstance(row['百分成绩'], (int, float)):
            grade = f"{row['百分成绩']}分"
        else:
            # 非数值类型的成绩直接转换为字符串
            grade = str(row['百分成绩'])
        grades_entry.append(f"{row['课程名称']}: {grade}")
    return grades_entry


def generate_email_content(student_name, grade_entries):
    # 根据学生姓名和成绩条目生成邮件内容
    grades_str = "\n".join(grade_entries)
    email_content = f"亲爱的{student_name}同学:\n\n" \
                    f"祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。\n\n" \
                    f"{grades_str}\n\n" \
                    "希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。\n\n" \
                    "再次恭喜您，祝您学习进步、事业成功！\n\n" \
                    "教务处"
    return email_content
