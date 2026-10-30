# Clone, Fetch, Pull

원격 저장소를 처음 가져오는 것과 이미 가진 저장소의 변경을 확인하고 반영하는 것은 다른 작업임. 세 명령이 어떤 위치를 바꾸는지 구분하면 원격과 로컬이 달라졌을 때 이유를 찾기 쉬움.

| 명령 | 하는 일 | 현재 작업 파일 |
| --- | --- | --- |
| `clone` | 원격 저장소의 파일과 이력을 받아 새 로컬 저장소 생성 | 새 폴더에 체크아웃 |
| `fetch` | 원격 이력을 받아 원격 추적 참조 갱신 | 기존 로컬 브랜치와 파일은 그대로 |
| `pull` | 원격 이력을 받은 뒤 현재 브랜치에 통합 | 통합 결과에 따라 변경 |

## 처음 가져올 때: clone

```powershell
git clone https://github.com/사용자이름/저장소이름.git
```

현재 위치에 새 폴더를 만들고 Git 이력과 작업 파일을 가져옴. 새 저장소에는 일반적으로 원본 주소가 `origin`으로 등록되므로 `git remote -v`로 확인할 수 있음. 이미 Git 저장소로 복제한 폴더에서 다시 `git init`할 필요는 없음.

GitHub에서 ZIP을 다운로드하면 파일 내용은 받을 수 있지만 일반적으로 Git 커밋 이력과 원격 연결은 포함되지 않음. 반대로 clone할 수 있다는 사실만으로 그 원본에 push할 권한이 생기는 것은 아님. 공개 코드의 사용과 수정은 해당 저장소의 라이선스도 확인함.

## 원격 변경을 가져와 살펴볼 때: fetch

```powershell
git fetch origin
git status -sb
git log --oneline --left-right main...origin/main
git diff main origin/main
```

`fetch`는 원격의 새 커밋 정보를 가져오고 `origin/main` 같은 원격 추적 참조를 갱신함. 로컬 `main`을 그 위치로 옮기거나 작업 파일을 자동으로 바꾸지는 않음. `git status`는 원격을 실시간 조회하는 명령이 아니므로 비교 전에 fetch해야 최근 원격 상태를 반영할 수 있음.

로그 비교의 `<`는 로컬 `main`에만 있는 커밋, `>`는 `origin/main`에만 있는 커밋을 나타냄. `diff main origin/main`은 두 브랜치 끝의 파일 내용 차이를 보여 줌. ahead는 로컬에만 커밋이 있다는 뜻, behind는 원격 추적 브랜치에만 커밋이 있다는 뜻임.

예를 들어 로컬과 `origin/main`이 C를 가리킬 때 GitHub에 D가 추가되면 내 로컬 정보는 여전히 C일 수 있음. fetch 후 `origin/main`은 D로 갱신되지만 로컬 `main`과 작업 파일은 C에 남음. 이때 차이를 확인하고 통합 여부를 정할 수 있음.

## 로컬 브랜치에 반영할 때: pull

```powershell
git status
git switch main
git pull --ff-only origin main
```

pull은 fetch 후 가져온 이력을 현재 브랜치에 통합함. `--ff-only`는 브랜치 위치를 앞으로 옮기는 fast-forward가 가능한 경우에만 진행함. 로컬과 원격에 각각 별도 커밋이 있어 이력이 갈라졌다면 중단하므로 그 차이를 확인하고 merge나 rebase 같은 통합 방법을 정해야 함.

일반 `git pull`의 통합 방식은 옵션과 설정에 따라 달라짐. `--rebase`를 사용하면 가져온 이력을 기준으로 로컬 작업을 다시 적용함. 통합 전에는 미커밋 변경을 확인하고 필요한 작업은 커밋이나 stash로 보관함.

## 통합 중 충돌이 나면

로컬과 원격에서 README의 같은 부분을 각기 수정했거나, 같은 이름의 파일을 양쪽에서 따로 추가했다면 자동 병합이 어려울 수 있음. 이때 Git은 병합을 중단하고 충돌 파일을 표시함. `git status`로 확인한 뒤 파일의 양쪽 내용을 읽고 최종 내용을 정함.

표시를 제거하고 저장한 다음 `git add <파일>`로 해결을 표시하고, merge가 진행 중이면 `git commit`으로 병합을 완료함. rebase 중이라면 `git rebase --continue`를 사용함. 해결 전에는 다시 pull해도 미해결 상태라는 오류가 나며 push도 아직 원격 이력을 통합하지 못해 거절될 수 있음. 무리하게 강제 push하지 않고 어떤 작업이 진행 중인지부터 확인함.

참고: [git clone](https://git-scm.com/docs/git-clone), [git fetch](https://git-scm.com/docs/git-fetch), [git pull](https://git-scm.com/docs/git-pull)

[이전](01-remote-and-push.md) | [다음](03-pull-request.md) | [목차로](../README.md)
