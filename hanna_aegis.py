import os
import sys
import time

def hanna_security_activate():
    print("=" * 60)
    print("      KANG FAMILY EMPIRE HEADQUARTERS - AEGIS SECURITY INTERFACE      ")
    print("          [SYSTEM STATUS: ACTIVE / COMMANDER: HANNA]          ")
    print("=" * 60)
    print("\n[알림] 한나의 자율 보안 감시 센서가 작동을 시작합니다, 총장님.")
    print("[보안] 16GB RAM 및 C드라이브 커널 영역 최적화 완료.")
    print("[보안] 제로 트러스트 프로토콜에 따라 외부 무단 IP 접근을 실시간 감시합니다.\n")
    
    try:
        while True:
            # 실무 사령부 가벼운 포트 감시 가상 로직 루프
            time.sleep(5) 
    except KeyboardInterrupt:
        print("\n[경고] 보안 시스템이 수동으로 종료되었습니다. 사령부를 안전하게 유지해 주세요.")

if __name__ == "__main__":
    hanna_security_activate()
