# Upload-GitHub Task Instructions

## Goal
Re-upload only the blocked GitHub `user-attachments` assets listed in `blocked-videos.yaml` so they are publicly accessible, then update both index and markdown references.

## Inputs
- `./.tasks/upload-github/blocked-videos.yaml`
- `./.tasks/upload-youtube/video-index.yaml`
- Markdown files under the repo root
- Local video files referenced by `local_file` in `blocked-videos.yaml`

## Output
- Updated `./.tasks/upload-youtube/video-index.yaml` with new `github_asset_url` values for blocked entries
- Updated markdown files where old blocked URLs are referenced
- A new file `./.tasks/upload-github/reupload-map.yaml` with old->new URL mapping and status

## Required workflow
1. Create/choose a **public** GitHub location for hosting attachments (public repo issue/discussion/release workflow).
2. For each `blocked_videos` entry:
   - Upload the `local_file` to that public GitHub context.
   - Capture the new public URL in the format `https://github.com/user-attachments/assets/<uuid>`.
   - Record mapping in `reupload-map.yaml`.
3. Update `./.tasks/upload-youtube/video-index.yaml`:
   - Find entry by exact old `github_asset_url`.
   - Replace only `github_asset_url` with the new URL.
   - Keep `filename`, `references`, `youtube_source`, and metadata unchanged.
4. Update markdown:
   - Replace exact old blocked URLs with new URLs.
   - Do not modify unrelated URLs.
5. Validate:
   - Every old blocked URL should have a new URL mapping.
   - No blocked URL remains in `video-index.yaml`.
   - No blocked URL remains in markdown files.

## Safety constraints
- Do not change YouTube links.
- Do not rename local files.
- Do not alter non-blocked `github_asset_url` entries.
- Preserve YAML structure and ordering as much as possible.

## Suggested validation commands
```bash
rg -n "39084f14-e65b-4fa1-a472-4baa73af7a01|cbed4a39-7773-4de1-bf57-921d7a5cac48|d12d417b-b93b-41a7-a231-9a2a4e925229|193b213d-a8fd-4f97-b9d0-6c32978bd268|2337609a-a49f-4495-b439-4dd729dc661d|60d9f5b6-f164-41c9-860c-5461250cbc1a|e69ab0f3-f6e5-46f7-9bab-1ecf86b0ba3e|291d8769-8aad-4e74-9b4d-7a010072f7ee|87cdcf71-4569-4361-82aa-d048068846d9|282e4e73-a2b8-4c19-8195-51e8736e45d5|9ca87915-2aad-4154-b9ed-2755d1ef4e26|c12bc774-7a13-4505-8a91-bc5b9076ca71|80a1dfe1-a1ea-43a9-be46-b3c6dcf952d0|f5f1d77a-3e82-4e92-af49-5a0ce1032aa9|278aacdb-682d-4c37-acb6-2604c87ff185|4f23359e-7b95-4837-a04c-cc0ea0f4e1eb|50518e79-56e0-4edc-93f4-2656500eea74|69b435d1-8854-4b21-a10a-18384da48d22|9287e03d-2f8a-4fbd-86de-639a24999e6e|d12c664c-bdb1-48b4-b2cf-c8262cf572b7|f2c9ddd9-089b-44e6-837c-850cd323dc76|a76a1e75-e618-4f29-bc6d-7604fabdc1df|51658d6d-92c6-4be1-9c35-58a5a88b6ec0" .
```

## Notes
- The blocked set comes from prior verified 404/non-public GitHub asset URLs in this session.
- If any `local_file` is missing, mark that entry as `missing_local_file: true` in `reupload-map.yaml`.
