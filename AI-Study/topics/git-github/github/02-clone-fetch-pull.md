# clone, fetch, pull

| 명령 | 하는 일 |
| --- | --- |
| `clone` | 파일과 이력을 받아 새 로컬 저장소 생성 |
| `fetch` | 원격 이력을 받고 원격 추적 정보 갱신 |
| `pull` | 원격 이력을 받은 뒤 현재 브랜치에 통합 |

## clone

```powershell
git clone https://github.com/jaemin-devlog/AI-Study.git
```

- clone 시 origin 자동 등록
- 이미 Git 저장소이므로 init은 불필요
- GitHub Download ZIP에는 Git 이력 없음
- clone과 원본 저장소의 push 권한은 별개

## fetch

```powershell
git fetch origin
git status -sb
```

- 원격 이력과 `origin/main` 갱신
- 로컬 main과 작업 파일은 유지
- status는 원격을 실시간 조회하지 않음

main과 origin/main에 커밋이 있을 때 이력 비교:

```powershell
git log --oneline --left-right main...origin/main
git diff main origin/main
```

- `<`: 로컬 main에만 있는 커밋
- `>`: origin/main에만 있는 커밋
- `diff`: 두 브랜치 끝의 파일 내용 차이
- `ahead`: 로컬에만 커밋 있음 / `behind`: 원격 추적 브랜치에만 커밋 있음

## pull

```powershell
git switch main
git pull --ff-only origin main
```

- 현재 브랜치에 원격 이력 통합. 미커밋 작업은 commit·stash로 정리
- `--ff-only`: 브랜치 위치만 앞으로 옮길 수 있을 때 반영
- 양쪽에 다른 커밋이 있으면 중단. merge·rebase 중 통합 방식 결정
- pull의 통합 방식은 옵션·설정에 따라 달라짐. `--rebase`는 rebase로 통합

참고: [git clone](https://git-scm.com/docs/git-clone), [git fetch](https://git-scm.com/docs/git-fetch), [git pull](https://git-scm.com/docs/git-pull)

[목차로](../README.md)
