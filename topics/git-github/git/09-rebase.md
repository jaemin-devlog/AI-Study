# Rebase

작업 브랜치를 만든 뒤 `main`에도 새로운 커밋이 생기면 두 이력이 갈라짐. merge는 두 흐름을 통합하고, rebase는 작업 브랜치의 커밋을 다른 기준 뒤에 다시 적용해 이력을 바꾸는 방법임.

## 작업 브랜치의 출발점 바꾸기

![Rebase 전후의 커밋](../assets/rebase.svg)

그림에서 작업 커밋 D와 E는 B에서 시작했지만 `main`은 C까지 진행했음. 작업 브랜치에서 `main`을 기준으로 rebase하면 D와 E의 변경을 C 뒤에 다시 적용한 D', E'가 만들어짐.

```powershell
git switch docs/git-note
git rebase main
```

현재 작업 브랜치를 이동시키는 명령임. `main` 자체는 C에 그대로 있고, `docs/git-note`가 새 E'를 가리킴. 새로 만들어진 커밋은 내용이 비슷해도 부모가 달라져 해시가 달라짐.

| 방식 | 이력의 변화 |
| --- | --- |
| Merge | 기존 흐름을 유지하며 병합 결과로 연결 |
| Rebase | 작업 커밋을 새 기준 뒤에 다시 적용해 새 이력 생성 |

다른 사람이 이미 받아 사용 중인 공유 커밋을 혼자 rebase하면 상대방의 이력과 어긋날 수 있음. 자신만 사용하는 작업 커밋에 먼저 적용하고, 공유된 이력을 바꿔야 한다면 팀의 합의가 필요함.

## 충돌을 해결하고 계속하기

재적용 중 같은 부분을 서로 다르게 수정했다면 충돌이 날 수 있음. `git status`로 멈춘 상태와 충돌 파일을 확인하고, 파일을 수정해 충돌 표시를 없앤 다음 스테이지에 등록함.

```powershell
git add README.md
git rebase --continue
```

여러 커밋을 재적용하므로 다음 커밋에서 다시 충돌하면 같은 과정을 반복함. 커밋 메시지 편집기가 열리면 내용을 확인하고 저장한 뒤 닫음. 진행 중인 rebase를 중단하려면 `git rebase --abort`를 사용함.

Rebase의 충돌 화면에서는 현재 재적용을 받는 기준 쪽과 다시 적용 중인 작업 커밋을 확인해야 함. `ours`와 `theirs`라는 이름을 merge 때의 브랜치 역할과 무조건 같다고 가정하지 말고 실제 충돌 내용을 읽어 최종 결과를 판단함.

## main에 반영하는 단계는 별도

rebase를 마쳐도 작업 브랜치가 이동한 것이며 `main`에 자동으로 반영된 것은 아님. 그동안 `main`이 추가로 이동하지 않았다면 다음처럼 fast-forward로 합칠 수 있음.

```powershell
git switch main
git merge --ff-only docs/git-note
```

`--ff-only`는 위치만 앞으로 옮길 수 있을 때 진행하고 이력이 다시 갈라졌다면 중단함. 로컬 `main`을 기준으로 rebase하므로 원격의 최신 변경이 필요한 작업이라면 먼저 fetch하고 어떤 이력을 기준으로 삼을지 확인해야 함.

참고: [Git rebase](https://git-scm.com/docs/git-rebase), [Git merge](https://git-scm.com/docs/git-merge)

[이전](08-merge-and-conflict.md) | [다음](10-ignore-and-files.md) | [목차로](../README.md)
