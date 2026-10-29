# remote와 push

- commit: 로컬 저장소에 기록
- push: 로컬 커밋을 원격 저장소로 전송
- 원격 주소 등록과 쓰기 권한은 별개

## origin, main, origin/main

| 이름 | 의미 |
| --- | --- |
| `origin` | 원격 저장소 주소의 별명 |
| `main` | 로컬 브랜치 |
| `origin/main` | 마지막으로 확인한 원격 main의 위치를 기록한 로컬 참조 |

## 원격 주소

저장소: [jaemin-devlog/AI-Study](https://github.com/jaemin-devlog/AI-Study)

```powershell
git remote add origin https://github.com/jaemin-devlog/AI-Study.git
git remote -v
```

- `remote add`: 원격 주소를 별명으로 등록
- `remote -v`: fetch·push 주소 확인
- `remote origin already exists`: origin이 이미 등록된 상태
- 주소만 바꿀 때는 `remote add` 대신 `remote set-url`

## push와 upstream

| 명령 | 결과 |
| --- | --- |
| `git push -u origin main` | main 전송, 추적할 원격 브랜치 설정 |
| `git push` | 설정된 업스트림으로 전송 |
| `git branch -vv` | 로컬 브랜치의 업스트림·커밋 확인 |

- `-u`: 업스트림 설정
- `non-fast-forward`: 원격 이력과 바로 연결되지 않아 push 거절. fetch 후 이력 차이 확인
- HTTPS 인증: Git Credential Manager·토큰 사용. Git 작업에 계정 비밀번호 사용 불가

참고: [git remote](https://git-scm.com/docs/git-remote), [git push](https://git-scm.com/docs/git-push), [GitHub 인증](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)

[목차로](../README.md)
