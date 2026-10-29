# 저장소 생성과 설정

## Git 버전

```powershell
git --version
```

## 커밋 작성자

```powershell
git config --global user.name "jaemin-devlog"
git config user.name
git config user.email
```

- `user.name`: 커밋에 기록되는 작성자 이름
- `user.email`: 커밋에 기록되는 이메일
- GitHub 로그인과 작성자 정보는 별개
- `--global`: 내 계정의 저장소에 적용할 기본값
- `--local`: 현재 저장소 설정. 같은 항목의 global 설정보다 우선

## 저장소 생성

```powershell
git init -b main
git status
```

- `git init -b main`: 현재 폴더에 저장소 생성, 첫 브랜치 이름은 `main`
- 초기 상태: 커밋 없음, GitHub 저장소 생성 안 됨
- 저장소 범위: `AI-Study` 전체. 주제 폴더도 같은 저장소에서 관리
- `git status`: 현재 브랜치·추적 여부·스테이지 상태 확인

참고: [git init](https://git-scm.com/docs/git-init), [Git 초기 설정](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup), [커밋 이메일 설정](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)

[목차로](../README.md)
