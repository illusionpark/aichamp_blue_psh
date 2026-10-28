# 호우 대응 보도자료 대시보드

2026-05-25 호우 대응에 관한 **가상** 3개 부처 보도자료를 검색하고 수치를 비교합니다.

- 웹페이지: `index.html` (부처·제목·본문 검색, 카드 요약, 결과 건수, 원문 모달, 매트릭스)
- 자료: `보도자료데이터.json` (UTF-8)
- 이미지: `hero.svg`
- Google Sheets: `config.js`에 공개 게시된 Sheets 임베드 URL 설정
- 검색 스크립트: `solution.py` (본문 검색 → `결과_<키워드>.csv`)

## GitHub Pages

저장소 Settings → Pages → Deploy from a branch → main / (root)를 선택합니다.
공개 주소: https://illusionpark.github.io/aichamp_blue_psh/

## Python 검색

```bash
python solution.py "인명피해"
python solution.py "1,820"
python solution.py
```

마지막 명령은 키워드를 대화형으로 입력합니다. `solution.py`와 `보도자료데이터.json`은 같은 폴더에 있어야 합니다.
CSV 헤더는 `번호,부처,제목,본문`이며 UTF-8 BOM으로 저장되어 Excel 한글 호환을 지원합니다.
키워드가 없으면 오류를 표시하고 검색 결과가 없으면 헤더만 포함한 CSV를 저장합니다.

## Google Sheets

`요약매트릭스.csv`를 Google Sheets에 가져온 다음 파일 → 공유 → 웹에 게시에서 삽입 URL을 얻어 `config.js`의 `SHEETS_EMBED_URL`에 입력하세요.
공개 URL이 없을 경우에도 HTML 매트릭스는 정상 표시됩니다.

**주의:** 동원 인원, 예산, 시각은 보도자료마다 집계 범위나 의미가 다르므로 수치를 합산하거나 동일한 범위로 해석해서는 안 됩니다.
