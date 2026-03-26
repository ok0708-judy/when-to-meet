import time
from datetime import timedelta

def countdown_timer():
    """倒數計時器 - 使用者可自行設定時間"""
    
    print("=" * 40)
    print("        倒數計時器")
    print("=" * 40)
    
    while True:
        try:
            # 取得使用者輸入
            total_seconds = input("\n請輸入時間（秒鐘）: ")
            total_seconds = int(total_seconds)
            
            if total_seconds <= 0:
                print("❌ 請輸入大於 0 的數字")
                continue
            
            break
        except ValueError:
            print("❌ 請輸入有效的數字")
    
    print(f"\n⏱️  開始倒數 {total_seconds} 秒...\n")
    time.sleep(1)
    
    # 倒數計時
    remaining = total_seconds
    while remaining > 0:
        # 轉換為分:秒 格式
        minutes = remaining // 60
        seconds = remaining % 60
        
        # 視覺化顯示
        time_str = f"{minutes:02d}:{seconds:02d}"
        
        # 根據剩餘時間改變顯示
        if remaining <= 10:
            print(f"⚠️  {time_str}", end='\r', flush=True)
        else:
            print(f"⏱️  {time_str}", end='\r', flush=True)
        
        time.sleep(1)
        remaining -= 1
    
    # 倒數完成
    print("\n")
    print("=" * 40)
    print("        ✅ 時間到！")
    print("=" * 40)
    print("\n🔔 計時已完成！\n")

if __name__ == "__main__":
    try:
        countdown_timer()
    except KeyboardInterrupt:
        print("\n\n⛔ 計時器已停止")
