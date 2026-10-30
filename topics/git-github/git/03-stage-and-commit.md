# Stage와 Commit

파일을 저장하면 작업 폴더에는 변경이 반영되지만 Git의 버전이 자동으로 생기지는 않음. 커밋에 넣을 상태를 먼저 선택하고 그 상태를 기록해야 함. 이때 구분할 세 곳이 작업 폴더, 스테이지, 로컬 저장소임.

## 세 영역에서 무엇이 달라질까?

| 영역 | 역할 |
| --- | --- |
| 작업 폴더 | 파일을 실제로 만들고 수정하는 곳 |
| 스테이지(index) | 다음 커밋에 넣을 파일 상태를 준비하는 곳 |
| 로컬 저장소 | 만들어진 커밋과 이력을 보관하는 곳 |

`git add`는 파일을 다른 폴더로 이동시키지 않음. 실행한 시점의 내용을 다음 커밋에 넣도록 스테이지에 반영함. `git commit`은 스테이지에 준비된 상태를 하나의 버전으로 기록함.

파일 A와 파일 B를 모두 수정했더라도 A만 `add`하면 B의 수정은 그 커밋에 들어가지 않음. 관련된 변경을 하나로 묶으면 나중에 목적을 이해하거나 되돌리기 쉬워짐.

![작업 폴더에서 스테이지를 거쳐 로컬 커밋으로 기록](../assets/작업-스테이지-커밋.svg)

그림의 화살표는 파일 자체를 옮기는 경로가 아니라 각 위치에 상태를 반영하는 순서임. `add` 뒤에도 파일은 작업 폴더에 남으며 수정할 수 있음. 그 뒤의 수정은 다시 `add`하기 전까지 기존 스테이지에 반영되지 않음.

## 상태를 확인하고 커밋 만들기

아래 명령은 Git 실습용 저장소에서 `README.md`를 만든 뒤 실행하는 흐름임. 각 명령이 어떤 상태를 바꾸는지 확인하면서 읽음.

```powershell
git status
git add README.md
git diff --staged
git commit -m "첫 학습 기록 추가"
git status
```

처음 상태에서 새 파일은 `Untracked files`에 나타남. Git이 아직 그 파일을 추적 대상으로 등록하지 않았다는 뜻임. `add` 후에는 `Changes to be committed`에서 다음 커밋에 들어갈 변경을 확인할 수 있음.

`git diff --staged`는 마지막 커밋과 스테이지를 비교함. 첫 커밋을 준비하는 경우에는 기존 커밋 없이 새로 추가된 내용이 표시됨. `commit -m`은 메시지와 함께 준비된 상태를 기록함. 그 후에 작업 폴더와 스테이지에 남은 변경이 없으면 `working tree clean`으로 표시됨.

## add한 뒤 파일을 다시 수정하면?

파일을 저장하고 `git add README.md`를 실행한 뒤 한 줄을 더 추가했다고 해보자. 스테이지에는 `add`를 실행했던 시점의 내용이 남고 새 줄은 작업 폴더에만 있음. 스테이지는 파일의 최신 내용을 자동으로 따라가지 않음.

따라서 같은 파일이 `Changes to be committed`와 `Changes not staged for commit`에 동시에 나타날 수 있음. 새 줄까지 커밋하려면 파일을 저장하고 `git add README.md`를 다시 실행함. `git diff`는 아직 스테이지에 넣지 않은 수정, `git diff --staged`는 이미 준비한 변경을 확인할 때 사용함.

## 파일 상태와 선택 범위

`Untracked`는 아직 추적하지 않는 새 파일, `Changes not staged for commit`은 추적 중인 파일의 미등록 수정이나 삭제, `Changes to be committed`는 등록된 변경임. 파일 삭제도 다음 커밋에 반영하려면 삭제된 상태를 스테이지에 등록해야 함.

`git add .`은 현재 폴더와 그 하위의 변경을 한꺼번에 등록함. 원하지 않는 파일이 섞이지 않았는지 먼저 확인함. VS Code Source Control의 Changes에서 `+`를 누르는 작업도 해당 변경을 스테이지에 올리는 과정임. 커밋 후에는 `git log`로 기록이 어떻게 연결되는지 확인할 수 있음.

참고: [git add](https://git-scm.com/docs/git-add), [git commit](https://git-scm.com/docs/git-commit), [git status](https://git-scm.com/docs/git-status)

[이전](02-init-and-config.md) | [다음](04-log-and-diff.md) | [목차로](../README.md)
