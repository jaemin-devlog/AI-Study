# Fork와 Pull Request

여러 사람이 같은 `main`에 변경을 바로 올리면 작업 목적을 검토하기 전에 코드가 반영될 수 있음. 작업 브랜치의 변경을 다른 브랜치에 반영해 달라고 제안하고, 차이를 보며 의견을 주고받는 GitHub 기능이 Pull Request, 줄여서 PR임.

## PR의 두 방향

| 항목 | 역할 | 예시 |
| --- | --- | --- |
| base | 변경을 받을 브랜치 | `main` |
| compare 또는 head | 변경을 제안하는 브랜치 | `docs/git-note` |

PR 화면은 두 브랜치의 차이를 보여 줌. 제목과 설명에 무엇을 바꿨는지, 왜 필요한지, 어떻게 확인했는지를 적으면 다른 사람이 변경 목적을 이해하기 쉬움. PR을 만들었다는 것과 실제로 병합했다는 것은 별도 단계임.

## 같은 저장소에서 작업하기

로컬 작업 브랜치에서 필요한 변경을 커밋한 뒤 해당 브랜치를 원격에 올림.

```powershell
git push -u origin docs/git-note
```

GitHub에서 base를 `main`, compare를 `docs/git-note`로 지정해 PR을 만듦. 리뷰 중 같은 작업 브랜치에 수정 커밋을 추가하고 다시 push하면 기존 PR의 변경 내용에도 반영됨. 원격에 직접 브랜치를 올릴 권한이 있다면 같은 저장소의 브랜치끼리 PR을 만들 수 있으며 fork가 필수는 아님.

리뷰에서 지적받은 내용은 의도를 확인하고 코드를 수정한 뒤 다시 확인함. PR은 검토와 의견 교환의 공간이고 merge는 선택한 변경을 대상 브랜치에 통합하는 동작임. 어떤 사람이 병합할 수 있는지는 저장소 권한과 설정에 따라 달라짐.

## 원본에 직접 쓰기 권한이 없다면

Fork는 원본 저장소의 복사본을 내 GitHub 계정에 만드는 것. Clone은 원격 저장소를 내 컴퓨터로 복제하는 것임. 둘은 저장 위치와 목적이 다름.

원본에 직접 push할 권한이 없는 공개 프로젝트라면 fork가 허용된 경우 내 계정에 fork하고, 그 복사본을 로컬에 clone해 작업할 수 있음. 내 fork의 브랜치에 push한 뒤 원본 저장소의 base 브랜치로 PR을 제안함. fork에 올렸다고 원본이 자동으로 바뀌지는 않음. 공개 저장소의 코드를 활용할 때는 라이선스를 확인함.

## GitHub에서 병합한 뒤 내 컴퓨터 갱신하기

PR을 GitHub에서 병합해도 내 로컬 `main`은 자동으로 이동하지 않음. 로컬 작업 상태를 확인한 뒤 원격의 변경을 가져와 반영함.

```powershell
git status
git switch main
git pull --ff-only origin main
```

fast-forward할 수 없는 상태라면 명령이 중단되므로 로컬과 원격의 이력을 비교해야 함. 작업 브랜치를 삭제하기 전에는 변경이 원하는 방식으로 반영됐는지 확인함. squash나 rebase 방식으로 병합하면 커밋 해시가 달라져 로컬의 `git branch -d`가 단순 병합 여부를 다르게 판단할 수도 있음.

참고: [PR 만들기](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request), [Fork](https://docs.github.com/en/pull-requests/reference/forks)

[이전](02-clone-fetch-pull.md) | [다음](04-tags-and-releases.md) | [목차로](../README.md)
