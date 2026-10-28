"""3개 부처 보도자료에서 키워드가 포함된 본문을 CSV로 추출합니다."""
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "보도자료데이터.json"

def main():
    if len(sys.argv) > 2:
        print('사용법: python solution.py "키워드"')
        sys.exit(1)
    try:
        keyword = (sys.argv[1] if len(sys.argv) == 2 else input("검색 키워드 1개: ")).strip()
    except (EOFError, KeyboardInterrupt):
        print("\n[오류] 입력이 취소됐습니다.")
        sys.exit(1)
    if not keyword:
        print("[오류] 키워드를 1개 입력하세요.")
        sys.exit(1)

    try:
        articles = json.loads(DATA.read_text(encoding="utf-8-sig"))
        if not isinstance(articles, list):
            raise ValueError("최상위 JSON은 배열이어야 합니다.")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"[오류] 데이터 파일을 읽지 못했습니다: {exc}")
        sys.exit(1)

    matched = [article for article in articles
               if keyword.casefold() in str(article.get("본문", "")).casefold()]
    safe_keyword = re.sub(r'[\\/:*?"<>|\x00-\x1f]', "_", keyword).rstrip(" .")[:90] or "검색"
    output = HERE / f"결과_{safe_keyword}.csv"

    with output.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["번호", "부처", "제목", "본문"])
        for article in matched:
            writer.writerow([article.get(k, "") for k in ("번호", "부처", "제목", "본문")])

    print(f"검색 키워드: {keyword}")
    print(f"검색 결과: {len(matched)}건")
    print(f"저장 파일: {output.name}")

if __name__ == "__main__":
    main()
