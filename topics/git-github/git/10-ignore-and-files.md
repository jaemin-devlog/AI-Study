# 제외할 파일과 파일 관리

실험을 진행하면 코드 외에도 가상환경, 캐시, 로그, 비밀 설정이 생김. 프로젝트에 필요한 이력과 컴퓨터에서 다시 만들 수 있는 파일을 구분해야 저장소를 불필요하게 키우거나 비밀값을 올리는 일을 줄일 수 있음.

## .gitignore는 어떤 파일에 적용될까?

`.gitignore`는 Git이 새로 추적하지 않을 파일 패턴을 정하는 파일임. 저장소의 규칙도 팀과 공유할 수 있도록 `.gitignore` 자체는 보통 커밋함.

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

`.venv/`는 가상환경 폴더, `__pycache__/`와 `*.pyc`는 Python 캐시, `*.log`는 로그 파일을 제외하는 패턴임. `!`는 앞의 제외 규칙에 대한 예외이므로 `.env.example`은 추적할 수 있음. 예시 파일에는 실제 비밀키가 아니라 필요한 항목 이름과 가짜 예시만 넣음.

중요한 점은 `.gitignore`가 이미 추적 중인 파일을 자동으로 추적 해제하거나 과거 커밋에서 제거하지 않는다는 것임. 새 파일이 제외됐는지는 `git status`와 ignore 규칙으로 확인함.

## 파일을 남기고 추적만 중단하기

이미 추적한 `.env`를 앞으로 제외하려면 ignore 규칙을 추가한 뒤 인덱스에서 제거할 수 있음.

```powershell
git rm --cached .env
git add .gitignore
git commit -m "환경 설정 파일 추적 제외"
```

`--cached`는 로컬 작업 폴더의 파일은 두고 저장소에서 제거하는 변경을 스테이지에 올림. 다른 사람이 그 제거 커밋을 적용하면 해당 추적 파일이 작업 폴더에서 제거될 수 있으므로 필요한 설정은 각자 보관해야 함. 과거 커밋에 들어간 내용은 그대로 남음. 이미 공개된 비밀키는 이 명령만으로 안전해지지 않으므로 폐기하고 교체해야 함.

## 이름 변경과 삭제도 기록하기

```powershell
git mv old-note.md new-note.md
git status
git commit -m "학습 기록 이름 변경"
```

`git mv`는 작업 파일의 이름을 바꾸고 그 변경을 스테이지에 등록함. 삭제할 때는 실습용 추적 파일을 대상으로 `git rm old-note.md`를 사용할 수 있으며 작업 폴더에서도 파일이 삭제됨. 삭제 역시 커밋하기 전과 후가 다르고 원격에 반영하려면 push해야 함. 과거 커밋에 기록된 상태까지 자동으로 지워지는 것은 아님.

Git은 빈 폴더 자체를 기록하지 않음. 빈 폴더를 남겨야 할 때 안에 `.gitkeep` 같은 빈 파일을 두는 관례가 있지만 Git의 특별한 기능은 아님.

## 실습 저장소를 정리할 때

파일 삭제, 로컬 저장소 삭제, GitHub 저장소 삭제는 서로 다른 작업임. 어느 쪽을 지우는지와 미커밋 변경, 마지막 커밋, 원격 주소를 먼저 확인해야 함. 로컬 폴더를 삭제해도 원격이 자동으로 삭제되지 않고 원격을 삭제해도 로컬이 자동으로 삭제되지 않음. 필요한 작업은 보관하고 더 이상 필요 없는 실습용 대상만 정리함.

참고: [Git gitignore](https://git-scm.com/docs/gitignore), [Git rm](https://git-scm.com/docs/git-rm), [Git mv](https://git-scm.com/docs/git-mv)

[이전](09-rebase.md) | [다음](../github/01-remote-and-push.md) | [목차로](../README.md)
