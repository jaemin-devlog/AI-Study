# 저장소 생성과 설정

Git은 모든 폴더의 변경을 자동으로 기록하지 않음. 버전 관리할 프로젝트 폴더에서 저장소를 초기화해야 그 폴더 안의 파일과 커밋을 관리할 수 있음.

## Git이 실행되는지 확인하기

```powershell
git --version
```

터미널에 설치된 Git 버전이 나오면 명령을 실행할 수 있는 상태임. 명령을 찾을 수 없다면 Git 설치와 터미널의 실행 환경을 확인함. VS Code의 터미널도 Git을 호출하므로 Git이 설치되어 있어야 함.

CLI는 터미널에 명령어를 입력하는 방식이고 GUI는 버튼과 메뉴로 조작하는 방식. VS Code의 Source Control과 SourceTree는 GUI임. 어느 쪽을 쓰더라도 현재 작업할 폴더와 저장소를 먼저 확인해야 함.

## 커밋 작성자 설정하기

```powershell
git config --global user.name "이름"
git config --global user.email "본인이 사용할 이메일"
git config user.name
git config user.email
```

`user.name`과 `user.email`은 새 커밋에 기록되는 작성자 정보임. GitHub 로그인이나 원격 저장소에 접근할 권한 자체를 설정하는 것은 아님. GitHub 계정에 연결해 활동을 표시하려면 해당 계정에서 사용할 커밋 이메일을 확인해야 함.

`--global`은 현재 사용자 계정의 저장소들에 적용할 기본값이고 `--local`은 현재 저장소에 적용함. 같은 항목이 둘 다 있으면 저장소의 local 설정이 우선함. 확인 명령은 현재 저장소에 적용되는 값을 보여 줌.

## 프로젝트 폴더에 저장소 만들기

실습용 새 폴더로 이동한 뒤 다음 명령을 실행함. 이미 사용 중인 저장소 안에 실습용 저장소를 또 만들지 않도록 현재 위치를 먼저 확인함.

```powershell
git init -b main
git status
```

`git init -b main`은 현재 폴더를 Git 저장소로 초기화하고 첫 브랜치 이름을 `main`으로 지정함. `.git` 폴더에 이력과 관리 정보가 들어감. 초기화만 한 시점에는 기록된 커밋이 아직 없으며 GitHub 저장소가 자동으로 생기는 것도 아님.

VS Code에서는 프로젝트 폴더를 연 뒤 Source Control의 저장소 초기화 기능으로 같은 작업을 시작할 수 있음. SourceTree에서도 폴더를 지정해 저장소를 생성할 수 있음. 이후 `git status` 또는 화면의 변경 목록으로 어떤 저장소와 브랜치를 보고 있는지 확인함.

## Python 실습 환경과 Git 저장소 구분하기

Python 패키지를 사용하는 실습에서는 프로젝트마다 가상환경을 만들어 라이브러리 버전을 관리할 수 있음. 가상환경 생성과 패키지 설치는 Git 커밋과 별개의 작업임.

실습 저장소와 같은 상위 폴더에 `venvs` 폴더를 만들고, 그 안에 환경을 두는 흐름은 다음과 같음. 이미 `venvs`가 있다면 폴더를 다시 만들 필요는 없음.

```powershell
uv --version
uv venv --python 3.11 venvs/git-cli-practice
uv pip install --python venvs/git-cli-practice scikit-learn
uv pip show --python venvs/git-cli-practice scikit-learn
```

첫 명령은 `uv`가 준비됐는지 확인하고, 둘째는 Python 3.11 환경을 지정한 경로에 만듦. 설치와 확인에도 같은 경로를 명시하므로 환경을 활성화하지 않고 대상을 지정할 수 있음. `show`의 Location이 예상한 환경 안인지 확인함. Python 파일을 실행할 때도 해당 환경의 Python 실행 파일을 사용하거나 VS Code에서 그 인터프리터를 선택해야 함.

실습 저장소 밖에 환경을 두면 설치된 라이브러리 파일이 해당 저장소의 변경 목록에 들어가지 않음. 환경을 프로젝트 안에 둘 수도 있지만 이때는 `.gitignore`로 추적 제외 여부를 확인함. 다음에는 파일을 저장한 뒤 스테이지와 커밋을 거치는 과정을 살펴봄.

참고: [git init](https://git-scm.com/docs/git-init), [Git 초기 설정](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup), [커밋 이메일 설정](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)

[이전](01-git-basics.md) | [다음](03-stage-and-commit.md) | [목차로](../README.md)
