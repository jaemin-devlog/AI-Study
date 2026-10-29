# 제외할 파일과 파일 정리

## .gitignore

새로 추적하지 않을 파일 패턴. 저장소 루트의 `.gitignore`에 기록.

```gitignore
.env
.env.*
!.env.example
.venv/
__pycache__/
*.pyc
private-materials/
*.log
```

- `!`: 제외 규칙의 예외
- `.env.example`: 실제 비밀값 없이 항목 이름과 예시만 작성
- 이미 추적 중인 파일에는 소급 적용 없음

## 파일은 남기고 추적만 중단

이미 추적 중인 `.env` 제외. `.gitignore`에 규칙 추가 후 추적 중단.

```powershell
git rm --cached .env
git add .gitignore
git commit -m "환경 설정 파일 추적 제외"
```

- 내 작업 폴더의 `.env` 유지
- 저장소에서 파일을 제거하는 변경을 커밋
- 과거 커밋의 내용은 유지. 공개한 비밀키는 별도 폐기·교체 필요

## 이름 변경

추적 중인 `topics/git-github/README.md` 대상. 변경할 이름 `topics/git-github/README-old.md`는 아직 없는 상태.

```powershell
git mv topics/git-github/README.md topics/git-github/README-old.md
git commit -m "학습 기록 파일 이름 변경"
```

`git mv`: 이름 변경과 스테이지 등록.

## 파일 삭제

삭제 대상: 더 이상 필요 없는 추적 파일.

```powershell
git rm topics/git-github/README.md
git commit -m "불필요한 학습 기록 삭제"
```

- 작업 폴더에서도 파일 삭제
- 삭제도 커밋으로 기록. 원격 반영에는 push 필요
- 과거 커밋의 파일은 유지

## 빈 폴더와 저장소

- 빈 폴더 자체는 Git 기록 대상에서 제외
- 폴더를 남기려면 안에 `.gitkeep` 같은 빈 파일 추가
- `.gitkeep`은 파일명 관례. Git의 특별한 기능 없음
- 로컬 저장소 삭제와 GitHub 저장소 삭제는 별도. 한쪽 삭제 시 다른 쪽은 유지
- 저장소 안의 파일 삭제·커밋과 저장소 전체 삭제도 별개

참고: [Git gitignore](https://git-scm.com/docs/gitignore) · [Git rm](https://git-scm.com/docs/git-rm) · [Git mv](https://git-scm.com/docs/git-mv)

[목차로](../README.md)
