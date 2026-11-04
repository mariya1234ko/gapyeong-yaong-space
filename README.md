# 가평 야옹이네 · 공간대여 홈페이지

## 확인하기
`index.html`을 브라우저에서 열어보세요. **캐러셀의 사진 목록은 로컬 서버가 필요합니다.** 폴더에서 `python3 -m http.server 8000`을 실행하고 `http://localhost:8000/`을 방문하세요.

## 사진 추가·삭제 (코딩 불필요)
1. GitHub에서 `photos-original/garden/`, `interior/`, `kitchen/`, `cats/` 중 해당 폴더로 이동합니다.
2. **Add file → Upload files**로 JPG/PNG/WebP 원본을 올리고 **Commit changes** 합니다. 삭제하려면 해당 파일을 열어 삭제하고 커밋합니다.
3. **Actions → Build photo galleries** 완료 후 `gallery.json`과 `images/`가 자동 갱신됩니다. Pages 반영까지 약간의 시간이 걸릴 수 있습니다.
4. 캐러셀 사진은 **파일명 오름차순**으로 표시됩니다. 예: `01-정원.jpg`, `02-정원.jpg`.
5. 처음 설정할 때 저장소 Settings → Actions → General → Workflow permissions에서 **Read and write permissions**가 허용되어야 자동 커밋이 가능합니다. 저장소의 기본 브랜치는 `main`으로 설정합니다.

원본 사진은 **공개 저장소에서 누구나 내려받을 수 있습니다.** GPS EXIF 등의 민감한 메타데이터는 원본 업로드 전에 제거하세요. 생성된 WebP 사진에는 원본 EXIF를 복사하지 않습니다.

## 사진 처리
Pillow 기반 GitHub Actions가 썸네일 320px, 캐러셀 1200px, 확대 2000px(각각 최대 가로폭) WebP를 만들고 `gallery.json`을 생성합니다. 원본보다 큰 이미지로 확대하지 않습니다. 원본 삭제 시 해당 이미지도 삭제합니다.

## 대표 사진
현재 `assets/representative.svg`는 **실제 사진이 아닌 임시 이미지**입니다. 대화 링크에 있는 사진 파일은 직접 접근할 수 없어 사용하지 않았습니다. 실제로 사용 권한이 있는 대표 사진을 받으면 교체해야 합니다. 현재 모든 대표 위치에 같은 임시 이미지를 사용합니다.

## 블로그 링크
개별 방송 관련 글 URL이 확인되지 않아 **네이버 블로그 관련 검색 링크**로 연결했습니다. 정확한 게시물 URL이 확인되면 교체하세요.

## 배포
GitHub `mariya1234ko/gapyeong-yaong-space` 새 저장소에 파일을 올리고 Settings → Pages → Deploy from a branch → `main` / root를 선택합니다. 기존 `mariya1234ko.github.io` 저장소와 별개입니다.

예상 주소: https://mariya1234ko.github.io/gapyeong-yaong-space/

## 법적·운영 안내
숙박 서비스 홍보는 포함하지 않았습니다. 실제 공간 이용 조건, 위치, 요금은 확정 후 기입하세요. 방송 이미지·기사 사진 등 제3자 저작물은 허가 없이 복제하지 마세요.

## v4 배경색 및 사진 수정
- 상단에 생기던 회색 띠는 대표 SVG 파일 안에 포함된 이미지 여백/헤더와 CSS 배경 크기 설정이 겹친 현상입니다.
- `assets/hero-photo.webp`는 임시 디자인 이미지에서 글자가 없는 사진 부분만 잘라 웹용으로 압축한 파일입니다.
- 페이지 배경은 따뜻한 크림색으로 통일했습니다. 영상 영역은 대비를 위해 녹색을 유지합니다.
- `sitemap.xml`은 이미 존재하므로 새로 만들지 않았습니다. 검색 엔진 사이트맵 파일명은 `site.xml`이 아니라 통상 `sitemap.xml`입니다.


## v5 검색엔진 최적화(SEO)
- `index.html`: 가평 야옹이네 브랜드를 앞세우고 `서울 근교 촌캉스` 키워드를 당일 공간대여 맥락에서 자연스럽게 추가했습니다.
- `space.html`: 고유한 제목과 설명, 본문 및 이미지 대체 설명을 추가했습니다.
- 두 페이지 모두 canonical, Open Graph(임시 대표 이미지 포함), robots 메타태그, Organization/WebPage JSON-LD를 적용했습니다.
- `sitemap.xml`: 두 페이지의 절대 URL이 포함되어 있습니다.
- `robots.txt`: 프로젝트 폴더에 포함되어 있지만 GitHub Pages 프로젝트 사이트의 robots.txt는 호스트 루트(`/robots.txt`)에서만 표준적으로 적용됩니다. 별도 루트 사이트를 수정하지 않으므로 네이버 서치어드바이저에서 프로젝트 URL의 수집/색인을 확인하세요.
- 임시 대표 이미지는 실제 공간 사진이 아닙니다. 실제 원본 사진을 확보하면 `assets/hero-photo.webp`와 각 캐러셀 사진을 교체하고 OG 이미지를 다시 지정하세요.
- 네이버 서치어드바이저에서 사이트 소유확인, 사이트맵 제출 및 수집 요청은 직접 진행해야 합니다. 검색 노출 및 순위는 보장되지 않습니다.
