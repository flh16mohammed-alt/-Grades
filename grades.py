"""
برنامج تقدير الطالب بناءً على الدرجة النهائية
Student Grade Evaluator
"""

def get_grade_rating(score):
    """
    تحويل الدرجة العددية إلى تقدير نصي
    
    المعاملات:
        score (float): درجة الطالب بين 0 و 100
    
    المخرجات:
        str: التقدير (ضعيف، جيد، جيد جداً، ممتاز)
    """
    if score >= 90:
        return "ممتاز"
    elif score >= 75:
        return "جيد جداً"
    elif score >= 60:
        return "جيد"
    else:
        return "ضعيف"


def is_valid_number(value):
    """
    التحقق من أن القيمة المدخلة رقم صحيح أو عشري موجب
    
    المعاملات:
        value (str): النص المدخل من المستخدم
    
    المخرجات:
        float or None: القيمة الرقمية أو None إذا كان المدخل غير صالح
    """
    try:
        # محاولة تحويل النص إلى رقم عشري
        num = float(value)
        return num
    except ValueError:
        return None


def main():
    """
    الوظيفة الرئيسية للبرنامج
    تتعامل مع حلقة الإدخال وعرض النتائج ومعالجة الأخطاء
    """
    print("=" * 40)
    print("   برنامج تقدير الطالب - Student Grade Evaluator")
    print("=" * 40)
    print("أدخل درجة الطالب (0-100) للحصول على التقدير")
    print("اكتب 'خروج' لإنهاء البرنامج")
    print("-" * 40)
    
    while True:
        # طلب إدخال من المستخدم
        user_input = input("\nأدخل الدرجة أو 'خروج': ").strip()
        
        # شرط الخروج
        if user_input == "خروج":
            print("\nشكراً لاستخدام البرنامج. وداعاً!")
            break
        
        # التحقق من أن الإدخال رقم صالح
        score = is_valid_number(user_input)
        
        if score is None:
            print("[خطأ] الرجاء إدخال رقم صحيح (مثل: 85) أو كتابة 'خروج'")
            continue
        
        # التحقق من نطاق الدرجة
        if score < 0 or score > 100:
            print(f"[خطأ] الدرجة {score} غير صالحة. يجب أن تكون بين 0 و 100")
            continue
        
        # حساب التقدير وعرضه
        rating = get_grade_rating(score)
        
        # عرض النتيجة بشكل منسق
        print("-" * 30)
        print(f"الدرجة: {score:.2f}")
        print(f"التقدير: {rating}")
        print("-" * 30)


# نقطة بداية البرنامج
if __name__ == "__main__":
    main()
